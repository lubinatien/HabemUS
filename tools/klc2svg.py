"""Draw keyboard pictures of an MSKLC .klc file as SVG, in the style of
keyboard-layout-editor.com.

Usage: python tools/klc2svg.py [HabemUS.klc] [docs]

Writes:
  keyboard.svg     every key with its normal, Shift, AltGr and Shift+AltGr characters
  vowels.svg       the accented vowel blocks of the AltGr layer
  dead-<name>.svg  what each key gives after a dead key
"""
import sys
import unicodedata
from pathlib import Path
from xml.sax.saxutils import escape

from klc2pkl import char, parse_klc

U = 54  # one key unit, in pixels
MARGIN = 12
FONT = "Segoe UI, Helvetica Neue, Arial, sans-serif"

GREY = "#9a9a9a"
BLACK = "#1a1a1a"
RED = "#d6301e"
CAP_EDGE = "#7f7f7f"
CAP_SIDE = "#cccccc"
CAP_TOP = "#fcfcfc"
MOD_TOP = "#e6e6e6"
PLATE = "#e9e9e9"

# ANSI rows: (VK name or modifier label, width in units)
ROWS = [
    [("OEM_3", 1)] + [(str(d), 1) for d in "1234567890"]
    + [("OEM_MINUS", 1), ("OEM_PLUS", 1), ("Backspace", 2)],
    [("Tab", 1.5)] + [(c, 1) for c in "QWERTYUIOP"] + [("OEM_4", 1), ("OEM_6", 1), ("OEM_5", 1.5)],
    [("Caps", 1.75)] + [(c, 1) for c in "ASDFGHJKL"] + [("OEM_1", 1), ("OEM_7", 1), ("Enter", 2.25)],
    [("Shift", 2.25)] + [(c, 1) for c in "ZXCVBNM"]
    + [("OEM_COMMA", 1), ("OEM_PERIOD", 1), ("OEM_2", 1), ("Shift", 2.75)],
    [("Ctrl", 1.25), ("Win", 1.25), ("Alt", 1.25), ("SPACE", 6.25),
     ("AltGr", 1.25), ("Win", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)],
]

INVISIBLE = {" ": "␣", " ": "NBSP", " ": "NNBSP"}

# Colour of each vowel block in vowels.svg
VOWEL_TINTS = {"a": "#fde2e0", "e": "#fdebd0", "i": "#ddf2dc", "u": "#dbe9fb", "o": "#ece0f7"}


def label(c):
    return INVISIBLE.get(c, c)


def base_vowel(c):
    """'é' -> 'e'"""
    return unicodedata.normalize("NFD", c)[0].lower()


class Layout:
    def __init__(self, klc_path):
        self.info, states, rows, self.deadkeys = parse_klc(klc_path)
        self.keys = {}  # VK -> {state: (char, is_dead)}
        for _, vk, _, values, _ in rows:
            entry = {}
            for state, token in zip(states, values):
                if token == "-1":
                    continue
                dead = token.endswith("@")
                c = token if len(token) == 1 else char(token.rstrip("@"))
                entry[state] = (c, dead)
            self.keys[vk] = entry

    def get(self, vk, state):
        return self.keys.get(vk, {}).get(state, ("", False))

    def dead_key_position(self, dead):
        for vk, entry in self.keys.items():
            for state, (c, is_dead) in entry.items():
                if is_dead and c == dead:
                    return vk, state
        return None, None


class Svg:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size, fill, anchor="start", weight="normal"):
        if s:
            self.add('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s" font-weight="%s">%s</text>'
                     % (x, y, size, fill, anchor, weight, escape(s)))

    def keycap(self, x, y, w, top=CAP_TOP, edge=CAP_EDGE):
        """A keycap at (x, y), w units wide. Returns the face box (x, y, w, h)."""
        pw, ph = w * U - 2, U - 2
        self.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="%s" stroke="%s"/>'
                 % (x + 1, y + 1, pw, ph, CAP_SIDE, edge))
        fx, fy, fw, fh = x + 7, y + 4, pw - 12, ph - 12
        self.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="%s" stroke="#d9d9d9"/>'
                 % (fx, fy, fw, fh, top))
        return fx, fy, fw, fh

    def render(self):
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="%s">\n'
                '<rect width="100%%" height="100%%" rx="10" fill="%s"/>\n%s\n</svg>\n'
                % (self.width, self.height, self.width, self.height, FONT, PLATE, "\n".join(self.parts)))


def legend_size(text, colour):
    if len(text) > 2:
        return 12
    if colour == RED or (text and unicodedata.category(text[0]) in ("Sk", "Lm")):
        return 22  # thin accents (ˇ ˚ ´ ¨) need to be bigger to be visible
    return 17


def four_legends(svg, face, top_left, bottom_left, top_right, bottom_right):
    """Each legend is (text, colour). Empty texts are skipped."""
    fx, fy, fw, fh = face
    svg.text(fx + 4, fy + 16, top_left[0], 15, top_left[1])
    svg.text(fx + 4, fy + fh - 5, bottom_left[0], 15, bottom_left[1])
    svg.text(fx + fw - 4, fy + 17, top_right[0], legend_size(*top_right), top_right[1], "end")
    svg.text(fx + fw - 4, fy + fh - 5, bottom_right[0], legend_size(*bottom_right), bottom_right[1], "end")


def draw_keyboard(layout, draw_key, height_extra=0):
    width = 15 * U + 2 * MARGIN
    svg = Svg(width, len(ROWS) * U + 2 * MARGIN + height_extra)
    for r, row in enumerate(ROWS):
        x = MARGIN
        for name, w in row:
            draw_key(svg, name, x, MARGIN + r * U, w)
            x += w * U
    return svg


def is_modifier(name):
    return name in ("Backspace", "Tab", "Caps", "Enter", "Shift", "Ctrl", "Win", "Alt", "AltGr", "Menu")


def draw_modifier(svg, name, x, y, w, highlight=False):
    face = svg.keycap(x, y, w, top="#fff3c4" if highlight else MOD_TOP)
    fx, fy, fw, fh = face
    svg.text(fx + fw / 2, fy + fh / 2 + 5, name, 13, BLACK if highlight else "#555", "middle")


def main_keyboard(layout):
    def draw_key(svg, name, x, y, w):
        if is_modifier(name):
            return draw_modifier(svg, name, x, y, w, highlight=name == "AltGr")
        face = svg.keycap(x, y, w)
        normal, shift = layout.get(name, "0")[0], layout.get(name, "1")[0]
        (ag, ag_dead), (sag, sag_dead) = layout.get(name, "6"), layout.get(name, "7")
        colour = lambda dead: RED if dead else BLACK
        if name == "SPACE":
            four_legends(svg, face, ("", GREY), ("", GREY), (label(sag), BLACK), (label(ag), BLACK))
            return
        # Letters show only their capital, like printed keycaps
        left = ((shift, GREY), ("", GREY)) if normal.isalpha() else ((shift, GREY), (normal, GREY))
        if not ag_dead and not sag_dead and ag.upper() == sag and ag != sag:
            right = (sag, BLACK), ("", BLACK)
        else:
            right = (label(sag), colour(sag_dead)), (label(ag), colour(ag_dead))
        four_legends(svg, face, left[0], left[1], right[0], right[1])

    svg = draw_keyboard(layout, draw_key, height_extra=74)
    draw_legend(svg, MARGIN, len(ROWS) * U + MARGIN + 14)
    return svg.render()


def draw_legend(svg, x, y):
    face = svg.keycap(x, y, 2.5)
    four_legends(svg, face, ("Shift", GREY), ("normal", GREY), ("Shift+AltGr", BLACK), ("AltGr", BLACK))
    tx = x + 2.5 * U + 14
    svg.text(tx, y + 20, "Grey: without AltGr (US QWERTY).   Black: with AltGr.", 14, "#444")
    svg.text(tx, y + 40, "Red: dead key, press it and then another key.", 14, RED)


def vowels_keyboard(layout):
    def draw_key(svg, name, x, y, w):
        if is_modifier(name):
            return draw_modifier(svg, name, x, y, w, highlight=name == "AltGr")
        ag, ag_dead = layout.get(name, "6")
        vowel = base_vowel(ag) if ag and not ag_dead else ""
        accented = vowel in VOWEL_TINTS and ag != vowel and name not in ("SPACE",)
        face = svg.keycap(x, y, w, top=VOWEL_TINTS[vowel] if accented else CAP_TOP)
        fx, fy, fw, fh = face
        normal = layout.get(name, "1")[0] if layout.get(name, "0")[0].isalpha() else layout.get(name, "0")[0]
        if name == "SPACE":
            return
        svg.text(fx + 4, fy + 16, normal, 15, GREY)
        if accented:
            svg.text(fx + fw / 2 + 4, fy + fh - 6, ag, 24, BLACK, "middle", "bold")

    return draw_keyboard(layout, draw_key).render()


DEAD_NAMES = {"^": "circumflex", "´": "acute", "¨": "diaeresis", "`": "grave", "~": "tilde",
              "ˇ": "caron", "˚": "ring", "¬": "symbols", "Ω": "greek"}


def dead_keyboard(layout, dead):
    table = {}
    for base, result in layout.deadkeys[dead]:
        table.setdefault(base, result)
    trigger_vk, trigger_state = layout.dead_key_position(dead)

    def draw_key(svg, name, x, y, w):
        if is_modifier(name):
            return draw_modifier(svg, name, x, y, w)
        normal, shift = layout.get(name, "0")[0], layout.get(name, "1")[0]
        lower, upper = table.get(normal, ""), table.get(shift, "")
        trigger = name == trigger_vk
        face = svg.keycap(x, y, w, top="#fde2e0" if trigger else (CAP_TOP if lower or upper else "#efefef"),
                          edge=RED if trigger else CAP_EDGE)
        if name == "SPACE":
            four_legends(svg, face, ("", GREY), ("", GREY), ("", BLACK), (label(lower), BLACK))
            return
        left_bottom = "" if normal.isalpha() else normal
        four_legends(svg, face, (shift, GREY), (left_bottom, GREY), (upper, BLACK), (lower, BLACK))

    return draw_keyboard(layout, draw_key).render()


def main():
    root = Path(__file__).resolve().parent.parent
    klc = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "HabemUS.klc"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else root / "docs"
    out.mkdir(parents=True, exist_ok=True)
    layout = Layout(klc)
    files = {"keyboard.svg": main_keyboard(layout), "vowels.svg": vowels_keyboard(layout)}
    for dead in layout.deadkeys:
        files["dead-%s.svg" % DEAD_NAMES.get(dead, "%04x" % ord(dead))] = dead_keyboard(layout, dead)
    for name, content in files.items():
        (out / name).write_text(content, encoding="utf-8", newline="\n")
    print("Wrote %d pictures to %s" % (len(files), out))


if __name__ == "__main__":
    main()
