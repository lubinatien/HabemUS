# HabemUS

A keyboard layout for writing French, Spanish and the other languages written in the Latin alphabet, on a standard US QWERTY keyboard.

Without AltGr, HabemUS **is** US QWERTY: same letters, same symbols, same Ctrl shortcuts. Everything else sits on **AltGr** (the right Alt key), and the accented letters are placed **around the letter they belong to**, so you can find them without memorizing a chart.

![HabemUS keyboard: every key with its normal, Shift, AltGr and Shift+AltGr characters](docs/keyboard.svg)

## The idea: accents around the letter

Each vowel gets a 2×2 block of keys on the AltGr layer (one colour per vowel):

![The AltGr layer's accented vowels, grouped in coloured blocks around their letter](docs/vowels.svg)

Three rules cover all of them:

1. **AltGr + the vowel gives its most common accent**: à é í ó ú.
2. **The grave accent is right below the acute**: é over è, ó over ò, ú over ù, í over ì.
3. **Circumflex and diaeresis are on the neighbouring key**: â ä next to a, ê ë next to e, ô ö next to o. For i and u they are in the block just to the left: î ï on Y H, û ü on T G.

The other letters sit on or near their base letter: **ç** on C, **ñ** on N, and **ã ă ș ț æ œ õ** on the rest of the bottom row. Shift + AltGr gives the capital (Á, Ç, Ñ…), and Caps Lock works with them too.

For French and Spanish, every accented letter you use daily is a single key press with AltGr: à é è ê ç ù ô î ï ë û œ, and á é í ó ú ñ ü ¿ ¡.

## Full AltGr layer

The keyboard picture at the top shows everything. The same layer as a searchable table:

<details>
<summary>AltGr layer as a table</summary>

Dead keys are in **bold**: press one, then a letter (see [Dead keys](#dead-keys)).

| Key | AltGr | Shift+AltGr | | Key | AltGr | Shift+AltGr |
|---|---|---|---|---|---|---|
| `` ` `` | **&#96;** | **~** | | `A` | à | À |
| `1` | ¡ | ¹ | | `S` | ä | Ä |
| `2` | ª | ² | | `D` | è | È |
| `3` | º | ³ | | `F` | ë | Ë |
| `4` | £ | ¥ | | `G` | ü | Ü |
| `5` | € | ¢ | | `H` | ï | Ï |
| `6` | **ˇ** caron | **^** circumflex | | `J` | ù | Ù |
| `7` | **˚** ring / dot | № | | `K` | ì | Ì |
| `8` | „ | ‚ | | `L` | ò | Ò |
| `9` | “ | ‘ | | `;` | ö | Ö |
| `0` | ” | ’ | | `'` | **´** acute | **¨** diaeresis |
| `-` | ß | **Ω** Greek | | `Z` | ã | Ã |
| `=` | × | ÷ | | `X` | ă | Ă |
| `Q` | á | Á | | `C` | ç | Ç |
| `W` | â | Â | | `V` | ș | Ș |
| `E` | é | É | | `B` | ț | Ț |
| `R` | ê | Ê | | `N` | ñ | Ñ |
| `T` | û | Û | | `M` | æ | Æ |
| `Y` | î | Î | | `,` | œ | Œ |
| `U` | ú | Ú | | `.` | õ | Õ |
| `I` | í | Í | | `/` | ¿ | … |
| `O` | ó | Ó | | `\` | **¬** symbols | ¦ |
| `P` | ô | Ô | | Space | narrow no-break space | no-break space |
| `[` | « | ‹ | | | | |
| `]` | » | › | | | | |

</details>

The two no-break spaces on AltGr+Space are for French spacing: `« texte »`, `Quoi ?`.

## Dead keys

Press the dead key, release it, then type a letter. Pressing it twice, or following it with Space, types the accent itself.

| Dead key | Keys | Letters it makes |
|---|---|---|
| **^** circumflex | Shift+AltGr+6 | â ê î ô û ŵ ŷ |
| **´** acute | AltGr+' | á é í ó ú ý ć ń ś ź ŕ ł, and ő ű after ö ü (AltGr+; / AltGr+G) |
| **¨** diaeresis | Shift+AltGr+' | ä ë ï ö ü ÿ ẅ ẍ ḧ ẗ |
| **&#96;** grave | AltGr+&#96; | à è ì ò ù, and ą ę į ǫ ų after ä ë ï ö ü (ogonek) |
| **~** tilde | Shift+AltGr+&#96; | ã ñ õ |
| **ˇ** caron | AltGr+6 | š č ž ř ě ň ď ť ľ ǎ ǐ ǒ ǔ ǧ ǩ ȟ ǰ ǯ ǚ |
| **˚** ring / dot above | AltGr+7 | å ů ż ċ ġ ė, and ı İ (Turkish dotless / dotted i) |
| **¬** symbols | AltGr+\ | see below |
| **Ω** Greek | Shift+AltGr+- | see below |

All of them also work with capital letters (Š, Å, Ő…).

In the pictures below, the dead key is outlined in red, each key shows what it gives after the dead key (Shift on top), and greyed keys give nothing.

### Symbols (AltGr+\ then…)

![Symbols dead key: what each key gives after AltGr and backslash](docs/dead-symbols.svg)

<details>
<summary>Symbols as a table</summary>

| Key | Gives | | Key | Gives | | Key | Gives |
|---|---|---|---|---|---|---|---|
| `-` | – en dash | | `c` | © | | `+` | ± |
| `_` | — em dash | | `r` | ® | | `=` | ≠ |
| `0` | ° | | `t` | ™ | | `~` | ≈ |
| `o` `O` | ø Ø | | `s` | § | | `<` `>` | ≤ ≥ |
| `S` | ẞ | | `p` | ¶ | | `8` | ∞ |
| `m` | µ (micro) | | `d` `D` | † ‡ | | `.` | • |
| `v` `x` | ✓ ✗ | | `%` | ‰ | | `1` | № |
| `h` `j` `k` `l` | ← ↓ ↑ → | | `H` `J` `K` `L` | ⇐ ⇓ ⇑ ⇒ | | `2` `3` `4` `5` `6` | ½ ⅓ ¼ ⅔ ¾ |

</details>

The arrows follow the Vim direction keys: h left, j down, k up, l right.

### Greek (Shift+AltGr+- then…)

Letters follow the Linux (X11) Greek dead key, plus final sigma on `c`:

![Greek dead key: what each key gives after Shift+AltGr+-](docs/dead-greek.svg)

<details>
<summary>Greek letters as a table</summary>

| a | b | c | d | e | f | g | h | i | j | k | l | m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| α | β | ς | δ | ε | φ | γ | η | ι | θ | κ | λ | μ |

| n | o | p | q | r | s | t | u | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ν | ο | π | χ | ρ | σ | τ | υ | ω | ξ | ψ | ζ |

</details>

Shift gives the capitals (Shift+C gives Σ). The same dead key also makes **superscripts** from the digits and `- = + [ ]` (x² → `2`, ⁻ → `-`), and **subscripts** from the shifted digits (H₂O → `@`). Space gives μ, and pressing the dead key twice gives Ω.

### Accent dead keys

<details>
<summary>Circumflex, acute, diaeresis, grave, tilde, caron and ring</summary>

**^ circumflex** (Shift+AltGr+6)
![Circumflex dead key](docs/dead-circumflex.svg)

**´ acute** (AltGr+')
![Acute dead key](docs/dead-acute.svg)

**¨ diaeresis** (Shift+AltGr+')
![Diaeresis dead key](docs/dead-diaeresis.svg)

**&#96; grave** (AltGr+&#96;)
![Grave dead key](docs/dead-grave.svg)

**&#126; tilde** (Shift+AltGr+&#96;)
![Tilde dead key](docs/dead-tilde.svg)

**ˇ caron** (AltGr+6)
![Caron dead key](docs/dead-caron.svg)

**˚ ring / dot above** (AltGr+7)
![Ring and dot above dead key](docs/dead-ring.svg)

These pictures only show keys typed without AltGr. The combinations that start from an AltGr letter (´ then ö → ő, &#96; then ä → ą…) are listed in the table above.

</details>

## Installing

### Windows (installed layout)

The repository holds the source, [`HabemUS.klc`](HabemUS.klc), not a prebuilt installer. To build one:

1. Install [Microsoft Keyboard Layout Creator 1.4](https://www.microsoft.com/en-us/download/details.aspx?id=102134). Windows may ask you to enable an older .NET Framework.
2. Open `HabemUS.klc`, then choose **Project → Build DLL and Setup Package**.
3. Run the generated `setup.exe`, then pick **English (United States) – HabemUS** in Windows' language settings.

### Portable, no installation (PKL)

[Portable Keyboard Layout](https://github.com/Portable-Keyboard-Layout/Portable-Keyboard-Layout) runs HabemUS on top of the standard US layout, without admin rights. It works from a USB stick.

1. Download PKL (**Code → Download ZIP**) and copy `pkl.exe`, `nonASCII.ini` and the `languages\` folder into a new folder.
2. Copy the contents of this repository's [`pkl/`](pkl/) folder into the same folder (`pkl.ini` and `layouts\habemus\`).
3. In Windows' language settings, add the **United States-International** keyboard (built into Windows, no admin rights needed), switch to it, and run `pkl.exe`.

Why United States-International: PKL needs a Windows layout where right Alt is a real AltGr, and plain US doesn't have one. US-International has the same letters as US. Its dead keys (`'` `"` `` ` `` `~` `^`) are handled by PKL, so they type normally while PKL runs, and act as dead keys again when it's paused. If you can only use plain US, regenerate the layout with `python tools/klc2pkl.py --fake-altgr` and empty `systemsDeadkeys` in `pkl.ini`. PKL then emulates AltGr itself, but the key can occasionally get stuck down; press right Alt again to release it.

Hold left Alt and press right Alt to pause or resume it. If a program shows the wrong characters, press Win+F12 to try another way of sending them. PKL is no longer maintained, and it can't type into programs running as administrator unless it runs as administrator too.

### Changing the layout

Edit `HabemUS.klc`, either in Keyboard Layout Creator or as text (it is UTF-16), then regenerate the PKL version and the pictures:

```
python tools/klc2pkl.py
python tools/klc2svg.py
```

The pictures in [`docs/`](docs/) are SVG files drawn from the `.klc`, in the style of [keyboard-layout-editor.com](http://www.keyboard-layout-editor.com/).

## Credits

HabemUS draws on two layouts: its design comes from qwerty-fr, and most of its characters from EurKEY.

### qwerty-fr

**[qwerty-fr](https://github.com/qwerty-fr/qwerty-fr)** by Paul (devnoname120) and Julien Blitte is a QWERTY layout for typing French and English. HabemUS takes from it:

- the core idea of placing each accent by its **position relative to its letter**. qwerty-fr puts the grave accent on the letter, the circumflex above, the diaeresis below and the acute to the left. HabemUS groups each vowel into a 2×2 block instead, with the acute on the letter, so that Spanish á é í ó ú are as direct as French à é
- the goal of being a strict superset of QWERTY: without AltGr, nothing changes
- accented capitals with Shift + AltGr and Caps Lock (É, Ç…), which AZERTY can't type
- the no-break space and narrow no-break space on AltGr+Space, for French typography. HabemUS puts the narrow one, the more common in French, without Shift
- a Greek dead key that follows the Linux standard, which qwerty-fr also uses

### EurKEY

HabemUS started from the character set of **[EurKEY](https://eurkey.steffen.bruentjen.eu/)** by Steffen Brüntjen, version 1.3. From EurKEY it keeps:

- the AltGr number row, quotation marks and punctuation: ¡ ª º £ €, ¹ ² ³ ¥ ¢, „ “ ” ‚ ‘ ’, « » ‹ ›, × ÷, ¿ …
- the contents of the circumflex, acute, diaeresis, grave and tilde dead keys
- the caron and ring/dot-above dead keys. HabemUS adds ů ė ı İ to the second one
- the idea of a symbol dead key on AltGr+\, with its arrows and fractions
- the superscripts, subscripts and Space → μ of the Greek dead key

Compared with EurKEY, HabemUS changes:

- the AltGr letter keys, rearranged into the "accents around the letter" blocks above. EurKEY favours Germanic and Nordic letters, while HabemUS favours French and Spanish
- ă ș ț for Romanian, ő ű for Hungarian, and the two no-break spaces (from qwerty-fr)
- the Greek letters, which follow the Linux standard (`dead_greek` in [libX11's Compose table](https://gitlab.freedesktop.org/xorg/lib/libx11/-/raw/master/nls/en_US.UTF-8/Compose.pre)), like qwerty-fr, instead of EurKEY's Windows mapping, plus ς
- the symbol dead key contents, which add dashes, ©, ®, ™ and the other symbols listed above

The portable version runs on [Portable Keyboard Layout](https://github.com/Portable-Keyboard-Layout/Portable-Keyboard-Layout) by Máté Farkas.
