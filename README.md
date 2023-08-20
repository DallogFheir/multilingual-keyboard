# Multilingual Keyboard

**Multilingual Keyboard** is an Autohotkey application that allows you to easily switch between keyboard layouts of different languages and scripts, and provides hotstrings for a variety of symbols.

## Usage

To use this app, you have to install [AutoHotkey](https://www.autohotkey.com/)
and download `src` directory from this repository. Then you can just run
the `main.ahk` file.

The app currently supports 5 keyboard layouts:

1. **default**, containing a variety of common-use symbols, but not modifying any standard keys
1. **Cyrillic**, containing the letters of the Cyrillic alphabet
1. **Greek**, containing the letters of the Greek alphabet
1. **IPA**, containing the symbols of the International Phonetic Alphabet
1. **flag**, containing the _regional indicator symbols_ used to produce flag emojis

You can switch between keyboards by pressing `Alt` + `Shift` + the keyboard's number, for example `Alt` + `Shift` + `5` for the flag keyboard.

Outside of keyboard layouts, Multilingual Keyboard enables hotstrings used to type various symbols. For example, to get the ♥ symbol, you can type `hearts\`.

The app also automatically converts letters followed by combining diacritics to pre-composed characters, if available.

Below you can find the documentation on available keyboard layouts and hotstrings.

To suspend the app, press `F2`.

## Modification

If you want to modify the app, you should get familiar with AutoHotkey documentation.

Each AHK file should start with 2 lines of comments: the first containing the name of the module, the second - the description. Optionally, on the third line, you can type `; UPPERCASE` to indicate that the module will contain lowercase and uppercase variants of characters.

Each AHK rule consists of the hotkey/hotstring, the `Send` clause, and `return` keyword. You can put a comment after the `Send` clause to describe the replacement symbol. If there is no comment, the symbol will not be included in the auto-generated documentation, unless it's the uppercase variant of another character.

If you want to create a new `common` module, you need to include it in the `common.ahk` file.

If you want to create a new keyboard layout, you need to add a conditional rule to the `main.ahk` file.

Provided for you is a Python script that can generate the documentation (`main.py docs`) and sort hotkeys/hotstrings alphabetically (according to their Unicode code point, but putting lowercase letters before their uppercase counterparts; `main.py sort`). To generate the documentation without this introduction, you can run `main.py docs -w`.

## Hotkeys & hotstrings

### Keyboards

#### Default

**Hotkey to switch to keyboard:** `Alt` + `Shift` + `1`

Default keyboard.

| Symbol | Uppercase |                                      Unicode                                      |   Description    | Hotstring / hotkey |
| :----: | :-------: | :-------------------------------------------------------------------------------: | :--------------: | :----------------: |
|   ó    |     Ó     | [U+00F3](https://codepoints.net/U+00F3) / [U+00D3](https://codepoints.net/U+00D3) |  _o_ with acute  |    `Alt` + `o`     |
|   þ    |     Þ     | [U+00FE](https://codepoints.net/U+00FE) / [U+00DE](https://codepoints.net/U+00DE) |      thorn       |    `Alt` + `t`     |
|   ą    |     Ą     | [U+0105](https://codepoints.net/U+0105) / [U+0104](https://codepoints.net/U+0104) | _a_ with ogonek  |    `Alt` + `a`     |
|   ć    |     Ć     | [U+0107](https://codepoints.net/U+0107) / [U+0106](https://codepoints.net/U+0106) |  _c_ with acute  |    `Alt` + `c`     |
|   ę    |     Ę     | [U+0119](https://codepoints.net/U+0119) / [U+0118](https://codepoints.net/U+0118) | _e_ with ogonek  |    `Alt` + `e`     |
|   ł    |     Ł     | [U+0142](https://codepoints.net/U+0142) / [U+0141](https://codepoints.net/U+0141) | _l_ with stroke  |    `Alt` + `l`     |
|   ń    |     Ń     | [U+0144](https://codepoints.net/U+0144) / [U+0143](https://codepoints.net/U+0143) |  _n_ with acute  |    `Alt` + `n`     |
|   ś    |     Ś     | [U+015B](https://codepoints.net/U+015B) / [U+015A](https://codepoints.net/U+015A) |  _s_ with acute  |    `Alt` + `s`     |
|   ź    |     Ź     | [U+017A](https://codepoints.net/U+017A) / [U+0179](https://codepoints.net/U+0179) |  _z_ with acute  |    `Alt` + `x`     |
|   ż    |     Ż     | [U+017C](https://codepoints.net/U+017C) / [U+017B](https://codepoints.net/U+017B) | _z_ with overdot |    `Alt` + `z`     |
|   ǫ    |     Ǫ     | [U+01EB](https://codepoints.net/U+01EB) / [U+01EA](https://codepoints.net/U+01EA) | _o_ with ogonek  |    `Alt` + `p`     |
|   ъ    |     Ъ     | [U+044A](https://codepoints.net/U+044A) / [U+042A](https://codepoints.net/U+042A) |    hard sign     |    `Alt` + `w`     |
|   ь    |     Ь     | [U+044C](https://codepoints.net/U+044C) / [U+042C](https://codepoints.net/U+042C) |    soft sign     |    `Alt` + `q`     |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Keyboards](#keyboards) | [Default](#default) ⬆️

#### Cyrillic

**Hotkey to switch to keyboard:** `Alt` + `Shift` + `2`

The Cyrillic alphabet.

| Symbol | Uppercase |                                      Unicode                                      |   Description    | Hotstring / hotkey |
| :----: | :-------: | :-------------------------------------------------------------------------------: | :--------------: | :----------------: |
|   а    |     А     | [U+0430](https://codepoints.net/U+0430) / [U+0410](https://codepoints.net/U+0410) |       _a_        |        `a`         |
|   б    |     Б     | [U+0431](https://codepoints.net/U+0431) / [U+0411](https://codepoints.net/U+0411) |       _be_       |        `b`         |
|   в    |     В     | [U+0432](https://codepoints.net/U+0432) / [U+0412](https://codepoints.net/U+0412) |       _ve_       |        `v`         |
|   г    |     Г     | [U+0433](https://codepoints.net/U+0433) / [U+0413](https://codepoints.net/U+0413) |       _ge_       |        `g`         |
|   д    |     Д     | [U+0434](https://codepoints.net/U+0434) / [U+0414](https://codepoints.net/U+0414) |       _de_       |        `d`         |
|   е    |     Е     | [U+0435](https://codepoints.net/U+0435) / [U+0415](https://codepoints.net/U+0415) |       _ye_       |        `e`         |
|   ж    |     Ж     | [U+0436](https://codepoints.net/U+0436) / [U+0416](https://codepoints.net/U+0416) |      _zhe_       |    `Alt` + `z`     |
|   з    |     З     | [U+0437](https://codepoints.net/U+0437) / [U+0417](https://codepoints.net/U+0417) |       _ze_       |        `z`         |
|   и    |     И     | [U+0438](https://codepoints.net/U+0438) / [U+0418](https://codepoints.net/U+0418) |       _i_        |        `i`         |
|   й    |     Й     | [U+0439](https://codepoints.net/U+0439) / [U+0419](https://codepoints.net/U+0419) |      _yot_       |        `y`         |
|   к    |     К     | [U+043A](https://codepoints.net/U+043A) / [U+041A](https://codepoints.net/U+041A) |       _ka_       |        `k`         |
|   л    |     Л     | [U+043B](https://codepoints.net/U+043B) / [U+041B](https://codepoints.net/U+041B) |       _el_       |        `l`         |
|   м    |     М     | [U+043C](https://codepoints.net/U+043C) / [U+041C](https://codepoints.net/U+041C) |       _em_       |        `m`         |
|   н    |     Н     | [U+043D](https://codepoints.net/U+043D) / [U+041D](https://codepoints.net/U+041D) |       _en_       |        `n`         |
|   о    |     О     | [U+043E](https://codepoints.net/U+043E) / [U+041E](https://codepoints.net/U+041E) |       _o_        |        `o`         |
|   п    |     П     | [U+043F](https://codepoints.net/U+043F) / [U+041F](https://codepoints.net/U+041F) |       _pe_       |        `p`         |
|   р    |     Р     | [U+0440](https://codepoints.net/U+0440) / [U+0420](https://codepoints.net/U+0420) |       _er_       |        `r`         |
|   с    |     С     | [U+0441](https://codepoints.net/U+0441) / [U+0421](https://codepoints.net/U+0421) |       _es_       |        `s`         |
|   т    |     Т     | [U+0442](https://codepoints.net/U+0442) / [U+0422](https://codepoints.net/U+0422) |       _te_       |        `t`         |
|   у    |     У     | [U+0443](https://codepoints.net/U+0443) / [U+0423](https://codepoints.net/U+0423) |       _u_        |        `u`         |
|   ф    |     Ф     | [U+0444](https://codepoints.net/U+0444) / [U+0424](https://codepoints.net/U+0424) |       _ef_       |        `f`         |
|   х    |     Х     | [U+0445](https://codepoints.net/U+0445) / [U+0425](https://codepoints.net/U+0425) |      _kha_       |        `h`         |
|   ц    |     Ц     | [U+0446](https://codepoints.net/U+0446) / [U+0426](https://codepoints.net/U+0426) |      _tse_       |        `c`         |
|   ч    |     Ч     | [U+0447](https://codepoints.net/U+0447) / [U+0427](https://codepoints.net/U+0427) |      _che_       |    `Alt` + `c`     |
|   ш    |     Ш     | [U+0448](https://codepoints.net/U+0448) / [U+0428](https://codepoints.net/U+0428) |      _sha_       |    `Alt` + `s`     |
|   щ    |     Щ     | [U+0449](https://codepoints.net/U+0449) / [U+0429](https://codepoints.net/U+0429) |     _shcha_      |    `Alt` + `d`     |
|   ъ    |     Ъ     | [U+044A](https://codepoints.net/U+044A) / [U+042A](https://codepoints.net/U+042A) |    hard sign     |    `Alt` + `q`     |
|   ы    |     Ы     | [U+044B](https://codepoints.net/U+044B) / [U+042B](https://codepoints.net/U+042B) |      _yeru_      |    `Alt` + `y`     |
|   ь    |     Ь     | [U+044C](https://codepoints.net/U+044C) / [U+042C](https://codepoints.net/U+042C) |    soft sign     |        `q`         |
|   э    |     Э     | [U+044D](https://codepoints.net/U+044D) / [U+042D](https://codepoints.net/U+042D) |       _e_        |    `Alt` + `e`     |
|   ю    |     Ю     | [U+044E](https://codepoints.net/U+044E) / [U+042E](https://codepoints.net/U+042E) |       _yu_       |    `Alt` + `u`     |
|   я    |     Я     | [U+044F](https://codepoints.net/U+044F) / [U+042F](https://codepoints.net/U+042F) |       _ya_       |    `Alt` + `f`     |
|   є    |     Є     | [U+0454](https://codepoints.net/U+0454) / [U+0404](https://codepoints.net/U+0404) |  Ukrainian _ye_  |    `Alt` + `r`     |
|   і    |     І     | [U+0456](https://codepoints.net/U+0456) / [U+0406](https://codepoints.net/U+0406) |    dotted _i_    |    `Alt` + `i`     |
|   ї    |     Ї     | [U+0457](https://codepoints.net/U+0457) / [U+0407](https://codepoints.net/U+0407) |       _yi_       |    `Alt` + `o`     |
|   ґ    |     Ґ     | [U+0491](https://codepoints.net/U+0491) / [U+0490](https://codepoints.net/U+0490) | _ge_ with upturn |    `Alt` + `g`     |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Keyboards](#keyboards) | [Cyrillic](#cyrillic) ⬆️

#### Greek

**Hotkey to switch to keyboard:** `Alt` + `Shift` + `3`

The Greek alphabet.

| Symbol | Uppercase |                                      Unicode                                      |   Description   | Hotstring / hotkey |
| :----: | :-------: | :-------------------------------------------------------------------------------: | :-------------: | :----------------: |
|   α    |     Α     | [U+03B1](https://codepoints.net/U+03B1) / [U+0391](https://codepoints.net/U+0391) |     _alpha_     |        `a`         |
|   β    |     Β     | [U+03B2](https://codepoints.net/U+03B2) / [U+0392](https://codepoints.net/U+0392) |     _beta_      |        `v`         |
|   γ    |     Γ     | [U+03B3](https://codepoints.net/U+03B3) / [U+0393](https://codepoints.net/U+0393) |     _gamma_     |        `g`         |
|   δ    |     Δ     | [U+03B4](https://codepoints.net/U+03B4) / [U+0394](https://codepoints.net/U+0394) |     _delta_     |        `d`         |
|   ε    |     Ε     | [U+03B5](https://codepoints.net/U+03B5) / [U+0395](https://codepoints.net/U+0395) |    _epsilon_    |        `e`         |
|   ζ    |     Ζ     | [U+03B6](https://codepoints.net/U+03B6) / [U+0396](https://codepoints.net/U+0396) |     _zeta_      |        `z`         |
|   η    |     Η     | [U+03B7](https://codepoints.net/U+03B7) / [U+0397](https://codepoints.net/U+0397) |      _eta_      |    `Alt` + `i`     |
|   θ    |     Θ     | [U+03B8](https://codepoints.net/U+03B8) / [U+0398](https://codepoints.net/U+0398) |     _theta_     |    `Alt` + `t`     |
|   ι    |     Ι     | [U+03B9](https://codepoints.net/U+03B9) / [U+0399](https://codepoints.net/U+0399) |     _iota_      |        `i`         |
|   κ    |     Κ     | [U+03BA](https://codepoints.net/U+03BA) / [U+039A](https://codepoints.net/U+039A) |     _kappa_     |        `k`         |
|   λ    |     Λ     | [U+03BB](https://codepoints.net/U+03BB) / [U+039B](https://codepoints.net/U+039B) |    _lambda_     |        `l`         |
|   μ    |     Μ     | [U+03BC](https://codepoints.net/U+03BC) / [U+039C](https://codepoints.net/U+039C) |      _mu_       |        `m`         |
|   ν    |     Ν     | [U+03BD](https://codepoints.net/U+03BD) / [U+039D](https://codepoints.net/U+039D) |      _nu_       |        `n`         |
|   ξ    |     Ξ     | [U+03BE](https://codepoints.net/U+03BE) / [U+039E](https://codepoints.net/U+039E) |      _xi_       |        `x`         |
|   ο    |     Ο     | [U+03BF](https://codepoints.net/U+03BF) / [U+039F](https://codepoints.net/U+039F) |    _omicron_    |        `o`         |
|   π    |     Π     | [U+03C0](https://codepoints.net/U+03C0) / [U+03A0](https://codepoints.net/U+03A0) |      _pi_       |        `p`         |
|   ρ    |     Ρ     | [U+03C1](https://codepoints.net/U+03C1) / [U+03A1](https://codepoints.net/U+03A1) |      _rho_      |        `r`         |
|   ς    |     Σ     | [U+03C2](https://codepoints.net/U+03C2) / [U+03A3](https://codepoints.net/U+03A3) | _sigma_ (final) |    `Alt` + `s`     |
|   σ    |     Σ     | [U+03C3](https://codepoints.net/U+03C3) / [U+03A3](https://codepoints.net/U+03A3) |     _sigma_     |        `s`         |
|   τ    |     Τ     | [U+03C4](https://codepoints.net/U+03C4) / [U+03A4](https://codepoints.net/U+03A4) |      _tau_      |        `t`         |
|   υ    |     Υ     | [U+03C5](https://codepoints.net/U+03C5) / [U+03A5](https://codepoints.net/U+03A5) |    _upsilon_    |        `u`         |
|   φ    |     Φ     | [U+03C6](https://codepoints.net/U+03C6) / [U+03A6](https://codepoints.net/U+03A6) |      _phi_      |        `f`         |
|   χ    |     Χ     | [U+03C7](https://codepoints.net/U+03C7) / [U+03A7](https://codepoints.net/U+03A7) |      _chi_      |        `h`         |
|   ψ    |     Ψ     | [U+03C8](https://codepoints.net/U+03C8) / [U+03A8](https://codepoints.net/U+03A8) |      _psi_      |    `Alt` + `p`     |
|   ω    |     Ω     | [U+03C9](https://codepoints.net/U+03C9) / [U+03A9](https://codepoints.net/U+03A9) |     _omega_     |    `Alt` + `o`     |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Keyboards](#keyboards) | [Greek](#greek) ⬆️

#### IPA

**Hotkey to switch to keyboard:** `Alt` + `Shift` + `4`

The International Phonetic Alphabet.

| Symbol |                 Unicode                 |                 Description                  |     Hotstring / hotkey     |
| :----: | :-------------------------------------: | :------------------------------------------: | :------------------------: |
|   æ    | [U+00E6](https://codepoints.net/U+00E6) |       near-open front unrounded vowel        |       `Shift` + `a`        |
|   ç    | [U+00E7](https://codepoints.net/U+00E7) |         voiceless palatal fricative          |        `Alt` + `c`         |
|   ð    | [U+00F0](https://codepoints.net/U+00F0) |           voiced dental fricative            |        `Alt` + `d`         |
|   ø    | [U+00F8](https://codepoints.net/U+00F8) |        close-mid front rounded vowel         |        `Alt` + `p`         |
|   ħ    | [U+0127](https://codepoints.net/U+0127) |        voiceless pharyngeal fricative        |       `Shift` + `h`        |
|   ŋ    | [U+014B](https://codepoints.net/U+014B) |              voiced velar nasal              |        `Alt` + `n`         |
|   œ    | [U+0153](https://codepoints.net/U+0153) |         open-mid front rounded vowel         |       `Shift` + `p`        |
|   ǀ    | [U+01C0](https://codepoints.net/U+01C0) |                 dental click                 |          `dclick`          |
|   ǁ    | [U+01C1](https://codepoints.net/U+01C1) |                lateral click                 |          `lclick`          |
|   ǂ    | [U+01C2](https://codepoints.net/U+01C2) |                palatal click                 |          `pclick`          |
|   ǃ    | [U+01C3](https://codepoints.net/U+01C3) |                alveolar click                |          `aclick`          |
|   ɐ    | [U+0250](https://codepoints.net/U+0250) |           near-open central vowel            |       `Shift` + `1`        |
|   ɑ    | [U+0251](https://codepoints.net/U+0251) |          open back unrounded vowel           |        `Alt` + `a`         |
|   ɒ    | [U+0252](https://codepoints.net/U+0252) |           open back rounded vowel            |       `Shift` + `o`        |
|   ɓ    | [U+0253](https://codepoints.net/U+0253) |          voiced bilabial implosive           |       `Shift` + `b`        |
|   ɔ    | [U+0254](https://codepoints.net/U+0254) |         open-mid back rounded vowel          |        `Alt` + `o`         |
|   ɕ    | [U+0255](https://codepoints.net/U+0255) | voiceless alveolo-palatal sibilant fricative |   `Alt` + `Shift` + `s`    |
|   ɖ    | [U+0256](https://codepoints.net/U+0256) |           voiced retroflex plosive           |       `Shift` + `d`        |
|   ɗ    | [U+0257](https://codepoints.net/U+0257) |          voiced alveolar implosive           |   `Alt` + `Shift` + `d`    |
|   ɘ    | [U+0258](https://codepoints.net/U+0258) |      close-mid central unrounded vowel       |   `Alt` + `Shift` + `i`    |
|   ə    | [U+0259](https://codepoints.net/U+0259) |              mid central vowel               |       `Shift` + `e`        |
|   ɛ    | [U+025B](https://codepoints.net/U+025B) |        open-mid front unrounded vowel        |        `Alt` + `e`         |
|   ɜ    | [U+025C](https://codepoints.net/U+025C) |       open-mid central unrounded vowel       |   `Alt` + `Shift` + `e`    |
|   ɞ    | [U+025E](https://codepoints.net/U+025E) |        open-mid central rounded vowel        |   `Alt` + `Shift` + `y`    |
|   ɟ    | [U+025F](https://codepoints.net/U+025F) |            voiced palatal plosive            |       `Shift` + `c`        |
|   ɠ    | [U+0260](https://codepoints.net/U+0260) |            voiced velar implosive            |          `vimplo`          |
|   ɢ    | [U+0262](https://codepoints.net/U+0262) |            voiced uvular plosive             |       `Shift` + `g`        |
|   ɣ    | [U+0263](https://codepoints.net/U+0263) |            voiced velar fricative            |        `Alt` + `g`         |
|   ɤ    | [U+0264](https://codepoints.net/U+0264) |        close-mid back unrounded vowel        |   `Alt` + `Shift` + `o`    |
|   ɥ    | [U+0265](https://codepoints.net/U+0265) |       voiced labio-palatal approximant       |       `Shift` + `w`        |
|   ɦ    | [U+0266](https://codepoints.net/U+0266) |           voiced glottal fricative           |        `Alt` + `h`         |
|   ɧ    | [U+0267](https://codepoints.net/U+0267) |                  _sj_-sound                  |            `6`             |
|   ɨ    | [U+0268](https://codepoints.net/U+0268) |        close central unrounded vowel         |       `Shift` + `i`        |
|   ɪ    | [U+026A](https://codepoints.net/U+026A) |       near-close front unrounded vowel       |        `Alt` + `i`         |
|   ɬ    | [U+026C](https://codepoints.net/U+026C) |     voiceless alveolar lateral fricative     |       `Shift` + `l`        |
|   ɭ    | [U+026D](https://codepoints.net/U+026D) |     voiced retroflex lateral approximant     |        `Alt` + `k`         |
|   ɮ    | [U+026E](https://codepoints.net/U+026E) |      voiced alveolar lateral fricative       |   `Alt` + `Shift` + `l`    |
|   ɯ    | [U+026F](https://codepoints.net/U+026F) |          close back unrounded vowel          |       `Shift` + `u`        |
|   ɰ    | [U+0270](https://codepoints.net/U+0270) |           voiced velar approximant           |       `Shift` + `2`        |
|   ɱ    | [U+0271](https://codepoints.net/U+0271) |          voiced labio-dental nasal           |        `Alt` + `m`         |
|   ɲ    | [U+0272](https://codepoints.net/U+0272) |             voiced palatal nasal             |       `Shift` + `n`        |
|   ɳ    | [U+0273](https://codepoints.net/U+0273) |            voiced retroflex nasal            |       `Shift` + `m`        |
|   ɴ    | [U+0274](https://codepoints.net/U+0274) |             voiced uvular nasal              |   `Alt` + `Shift` + `n`    |
|   ɵ    | [U+0275](https://codepoints.net/U+0275) |       close-mid central rounded vowel        |       `Shift` + `y`        |
|   ɶ    | [U+0276](https://codepoints.net/U+0276) |           open front rounded vowel           |   `Alt` + `Shift` + `p`    |
|   ɸ    | [U+0278](https://codepoints.net/U+0278) |         voiceless bilabial fricative         |        `Alt` + `f`         |
|   ɹ    | [U+0279](https://codepoints.net/U+0279) |         voiced alveolar approximant          |   `Alt` + `Shift` + `r`    |
|   ɺ    | [U+027A](https://codepoints.net/U+027A) |         voiced alveolar lateral flap         |   `Alt` + `Shift` + `k`    |
|   ɻ    | [U+027B](https://codepoints.net/U+027B) |         voiced retroflex approximant         |   `Alt` + `Shift` + `f`    |
|   ɽ    | [U+027D](https://codepoints.net/U+027D) |            voiced retroflex flap             |       `Shift` + `3`        |
|   ɾ    | [U+027E](https://codepoints.net/U+027E) |             voiced alveolar flap             |        `Alt` + `r`         |
|   ʀ    | [U+0280](https://codepoints.net/U+0280) |             voiced uvular trill              |       `Shift` + `f`        |
|   ʁ    | [U+0281](https://codepoints.net/U+0281) |           voiced uvular fricative            |       `Shift` + `r`        |
|   ʂ    | [U+0282](https://codepoints.net/U+0282) |    voiceless retroflex sibilant fricative    |       `Shift` + `s`        |
|   ʃ    | [U+0283](https://codepoints.net/U+0283) |      voiceless post-alveolar fricative       |        `Alt` + `s`         |
|   ʄ    | [U+0284](https://codepoints.net/U+0284) |           voiced palatal implosive           |          `pimplo`          |
|   ʈ    | [U+0288](https://codepoints.net/U+0288) |         voiceless retroflex plosive          |       `Shift` + `t`        |
|   ʉ    | [U+0289](https://codepoints.net/U+0289) |         close central rounded vowel          |   `Alt` + `Shift` + `u`    |
|   ʊ    | [U+028A](https://codepoints.net/U+028A) |      near-close near-back rounded vowel      |        `Alt` + `u`         |
|   ʋ    | [U+028B](https://codepoints.net/U+028B) |        voiced labiodental approximant        |        `Alt` + `v`         |
|   ʌ    | [U+028C](https://codepoints.net/U+028C) |        open-mid back unrounded vowel         |   `Alt` + `Shift` + `a`    |
|   ʍ    | [U+028D](https://codepoints.net/U+028D) |       voiceless labio-velar fricative        |        `Alt` + `w`         |
|   ʎ    | [U+028E](https://codepoints.net/U+028E) |      voiced palatal lateral approximant      |        `Alt` + `l`         |
|   ʏ    | [U+028F](https://codepoints.net/U+028F) |        near-close front rounded vowel        |        `Alt` + `y`         |
|   ʐ    | [U+0290](https://codepoints.net/U+0290) |     voiced retroflex sibilant fricative      |       `Shift` + `z`        |
|   ʑ    | [U+0291](https://codepoints.net/U+0291) |  voiced alveolo-palatal sibilant fricative   |   `Alt` + `Shift` + `z`    |
|   ʒ    | [U+0292](https://codepoints.net/U+0292) |        voiced post-alveolar fricative        |        `Alt` + `z`         |
|   ʔ    | [U+0294](https://codepoints.net/U+0294) |                 glottal stop                 |        `Alt` + `q`         |
|   ʕ    | [U+0295](https://codepoints.net/U+0295) |        voiced pharyngeal approximant         |       `Shift` + `q`        |
|   ʘ    | [U+0298](https://codepoints.net/U+0298) |                bilabial click                |          `bclick`          |
|   ʙ    | [U+0299](https://codepoints.net/U+0299) |                bilabial trill                |   `Alt` + `Shift` + `b`    |
|   ʛ    | [U+029B](https://codepoints.net/U+029B) |           voiced uvular implosive            |          `uimplo`          |
|   ʜ    | [U+029C](https://codepoints.net/U+029C) |          voiceless pharyngeal trill          |       `Shift` + `x`        |
|   ʝ    | [U+029D](https://codepoints.net/U+029D) |           voiced palatal fricative           |        `Alt` + `j`         |
|   ʟ    | [U+029F](https://codepoints.net/U+029F) |       voiced velar lateral approximant       |       `Shift` + `k`        |
|   ʡ    | [U+02A1](https://codepoints.net/U+02A1) |              pharyngeal plosive              |       `Shift` + `5`        |
|   ʢ    | [U+02A2](https://codepoints.net/U+02A2) |           voiced pharyngeal trill            |   `Alt` + `Shift` + `x`    |
|   ʰ    | [U+02B0](https://codepoints.net/U+02B0) |                  aspirated                   |   `Alt` + `Shift` + `h`    |
|   ʱ    | [U+02B1](https://codepoints.net/U+02B1) |               voiced aspirated               |       `Shift` + `j`        |
|   ʲ    | [U+02B2](https://codepoints.net/U+02B2) |                 palatalized                  |   `Alt` + `Shift` + `j`    |
|   ʷ    | [U+02B7](https://codepoints.net/U+02B7) |                  labialized                  |   `Alt` + `Shift` + `w`    |
|   ʼ    | [U+02BC](https://codepoints.net/U+02BC) |                   ejective                   |       `Shift` + `'`        |
|   ˀ    | [U+02C0](https://codepoints.net/U+02C0) |                 glottalized                  |   `Alt` + `Shift` + `q`    |
|   ˈ    | [U+02C8](https://codepoints.net/U+02C8) |                primary stress                |            `'`             |
|   ˌ    | [U+02CC](https://codepoints.net/U+02CC) |               secondary stress               | `Alt` + `Shift` + `` `; `` |
|   ː    | [U+02D0](https://codepoints.net/U+02D0) |                     long                     |          `` `; ``          |
|   ˑ    | [U+02D1](https://codepoints.net/U+02D1) |                  half-long                   |         `halflong`         |
|   ˕    | [U+02D5](https://codepoints.net/U+02D5) |               lowered (beside)               |       `Shift` + `9`        |
|   ˖    | [U+02D6](https://codepoints.net/U+02D6) |              advanced (beside)               |       `Shift` + `=`        |
|   ˗    | [U+02D7](https://codepoints.net/U+02D7) |              retracted (beside)              |         `sretract`         |
|   ˞    | [U+02DE](https://codepoints.net/U+02DE) |                 _r_-colored                  |       `Shift` + `4`        |
|   ˠ    | [U+02E0](https://codepoints.net/U+02E0) |                  velarized                   |   `Alt` + `Shift` + `g`    |
|   ˡ    | [U+02E1](https://codepoints.net/U+02E1) |               lateral release                |           `lrel`           |
|   ˣ    | [U+02E3](https://codepoints.net/U+02E3) |      voiceless velar fricative release       |          `vvfrel`          |
|   ˤ    | [U+02E4](https://codepoints.net/U+02E4) |                pharyngealized                |           `phar`           |
|   ˥    | [U+02E5](https://codepoints.net/U+02E5) |            high Chao tone letter             |            `1`             |
|   ˦    | [U+02E6](https://codepoints.net/U+02E6) |          half-high Chao tone letter          |            `2`             |
|   ˧    | [U+02E7](https://codepoints.net/U+02E7) |             mid Chao tone letter             |            `3`             |
|   ˨    | [U+02E8](https://codepoints.net/U+02E8) |          half-low Chao tone letter           |            `4`             |
|   ˩    | [U+02E9](https://codepoints.net/U+02E9) |             low Chao tone letter             |            `5`             |
|   ◌̈   | [U+0308](https://codepoints.net/U+0308) |                 centralized                  |     `Shift` + `` `; ``     |
|   ◌̍   | [U+030D](https://codepoints.net/U+030D) |               syllabic (above)               |       `Shift` + `0`        |
|   ◌̘   | [U+0318](https://codepoints.net/U+0318) |             advanced tongue root             |        `Alt` + `\`         |
|   ◌̙   | [U+0319](https://codepoints.net/U+0319) |            retracted tongue root             |   `Alt` + `Shift` + `\`    |
|   ◌̚   | [U+031A](https://codepoints.net/U+031A) |              no audible release              |            `7`             |
|   ◌̜   | [U+031C](https://codepoints.net/U+031C) |             less rounded (below)             |          `lround`          |
|   ◌̝   | [U+031D](https://codepoints.net/U+031D) |                    raised                    |            `8`             |
|   ◌̞   | [U+031E](https://codepoints.net/U+031E) |               lowered (below)                |            `9`             |
|   ◌̟   | [U+031F](https://codepoints.net/U+031F) |               advanced (below)               |            `=`             |
|   ◌̠   | [U+0320](https://codepoints.net/U+0320) |              retracted (below)               |         `retract`          |
|   ◌̥   | [U+0325](https://codepoints.net/U+0325) |                  voiceless                   |            `0`             |
|   ◌̩   | [U+0329](https://codepoints.net/U+0329) |               syllabic (below)               |       `Shift` + `-`        |
|   ◌̪   | [U+032A](https://codepoints.net/U+032A) |                dental (below)                |       `Shift` + `[`        |
|   ◌̬   | [U+032C](https://codepoints.net/U+032C) |                    voiced                    |          `voiced`          |
|   ◌̯   | [U+032F](https://codepoints.net/U+032F) |                 non-syllabic                 |       `Shift` + `6`        |
|   ◌̰   | [U+0330](https://codepoints.net/U+0330) |                creaky voiced                 |       `Shift` + `7`        |
|   ◌̴   | [U+0334](https://codepoints.net/U+0334) |          velarized / pharyngealized          |          `` ` ``           |
|   ◌̹   | [U+0339](https://codepoints.net/U+0339) |             more rounded (below)             |          `mround`          |
|   ◌̺   | [U+033A](https://codepoints.net/U+033A) |                    apical                    |       `Shift` + `]`        |
|   ◌̼   | [U+033C](https://codepoints.net/U+033C) |                 linguolabial                 |         `linglab`          |
|   ◌̽   | [U+033D](https://codepoints.net/U+033D) |               mid-centralized                |        `midcentral`        |
|   ◌͆   | [U+0346](https://codepoints.net/U+0346) |                    dental                    |        `Alt` + `[`         |
|   ◌͑   | [U+0351](https://codepoints.net/U+0351) |             less rounded (above)             |         `alround`          |
|   ◌͗   | [U+0357](https://codepoints.net/U+0357) |             more rounded (above)             |         `amround`          |
|   ◌͜   | [U+035C](https://codepoints.net/U+035C) |              affricate (below)               |          `affric`          |
|   ◌͡   | [U+0361](https://codepoints.net/U+0361) |              affricate (above)               |            `,`             |
|   β    | [U+03B2](https://codepoints.net/U+03B2) |          voiced bilabial fricative           |        `Alt` + `b`         |
|   θ    | [U+03B8](https://codepoints.net/U+03B8) |          voiceless dental fricative          |        `Alt` + `t`         |
|   χ    | [U+03C7](https://codepoints.net/U+03C7) |          voiceless uvular fricative          |        `Alt` + `x`         |
|   ᵊ    | [U+1D4A](https://codepoints.net/U+1D4A) |          mid central vowel release           |          `mdvrel`          |
|   ᶑ    | [U+1D91](https://codepoints.net/U+1D91) |          voiced retroflex implosive          |   `Alt` + `Shift` + `t`    |
|   ᶿ    | [U+1DBF](https://codepoints.net/U+1DBF) |      voiceless dental fricative release      |          `vdfrel`          |
|   ‖    | [U+2016](https://codepoints.net/U+2016) |           major (intonation) break           |            `\`             |
|   ‿    | [U+203F](https://codepoints.net/U+203F) |                   linking                    |   `Alt` + `Shift` + `m`    |
|   ⁼    | [U+207C](https://codepoints.net/U+207C) |                 unaspirated                  |            `-`             |
|   ⁿ    | [U+207F](https://codepoints.net/U+207F) |                nasal release                 |           `nrel`           |
|   ↘    | [U+2198](https://codepoints.net/U+2198) |                 global fall                  |   `Alt` + `Shift` + `,`    |
|   ⱱ    | [U+2C71](https://codepoints.net/U+2C71) |           voiced labiodental flap            |       `Shift` + `v`        |
|   ꜛ    | [U+A71B](https://codepoints.net/U+A71B) |                    upstep                    |       `Shift` + `.`        |
|   ꜜ    | [U+A71C](https://codepoints.net/U+A71C) |                   downstep                   |       `Shift` + `,`        |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Keyboards](#keyboards) | [IPA](#ipa) ⬆️

#### Flags

**Hotkey to switch to keyboard:** `Alt` + `Shift` + `5`

The regional indicator symbols that can be combined into flag emojis.

| Symbol |                  Unicode                  |           Description           | Hotstring / hotkey |
| :----: | :---------------------------------------: | :-----------------------------: | :----------------: |
|   🇦    | [U+1F1E6](https://codepoints.net/U+1F1E6) | _A_ (regional indicator symbol) |        `a`         |
|   🇧    | [U+1F1E7](https://codepoints.net/U+1F1E7) | _B_ (regional indicator symbol) |        `b`         |
|   🇨    | [U+1F1E8](https://codepoints.net/U+1F1E8) | _C_ (regional indicator symbol) |        `c`         |
|   🇩    | [U+1F1E9](https://codepoints.net/U+1F1E9) | _D_ (regional indicator symbol) |        `d`         |
|   🇪    | [U+1F1EA](https://codepoints.net/U+1F1EA) | _E_ (regional indicator symbol) |        `e`         |
|   🇫    | [U+1F1EB](https://codepoints.net/U+1F1EB) | _F_ (regional indicator symbol) |        `f`         |
|   🇬    | [U+1F1EC](https://codepoints.net/U+1F1EC) | _G_ (regional indicator symbol) |        `g`         |
|   🇭    | [U+1F1ED](https://codepoints.net/U+1F1ED) | _H_ (regional indicator symbol) |        `h`         |
|   🇮    | [U+1F1EE](https://codepoints.net/U+1F1EE) | _I_ (regional indicator symbol) |        `i`         |
|   🇯    | [U+1F1EF](https://codepoints.net/U+1F1EF) | _J_ (regional indicator symbol) |        `j`         |
|   🇰    | [U+1F1F0](https://codepoints.net/U+1F1F0) | _K_ (regional indicator symbol) |        `k`         |
|   🇱    | [U+1F1F1](https://codepoints.net/U+1F1F1) | _L_ (regional indicator symbol) |        `l`         |
|   🇲    | [U+1F1F2](https://codepoints.net/U+1F1F2) | _M_ (regional indicator symbol) |        `m`         |
|   🇳    | [U+1F1F3](https://codepoints.net/U+1F1F3) | _N_ (regional indicator symbol) |        `n`         |
|   🇴    | [U+1F1F4](https://codepoints.net/U+1F1F4) | _O_ (regional indicator symbol) |        `o`         |
|   🇵    | [U+1F1F5](https://codepoints.net/U+1F1F5) | _P_ (regional indicator symbol) |        `p`         |
|   🇶    | [U+1F1F6](https://codepoints.net/U+1F1F6) | _Q_ (regional indicator symbol) |        `q`         |
|   🇷    | [U+1F1F7](https://codepoints.net/U+1F1F7) | _R_ (regional indicator symbol) |        `r`         |
|   🇸    | [U+1F1F8](https://codepoints.net/U+1F1F8) | _S_ (regional indicator symbol) |        `s`         |
|   🇹    | [U+1F1F9](https://codepoints.net/U+1F1F9) | _T_ (regional indicator symbol) |        `t`         |
|   🇺    | [U+1F1FA](https://codepoints.net/U+1F1FA) | _U_ (regional indicator symbol) |        `u`         |
|   🇻    | [U+1F1FB](https://codepoints.net/U+1F1FB) | _V_ (regional indicator symbol) |        `v`         |
|   🇼    | [U+1F1FC](https://codepoints.net/U+1F1FC) | _W_ (regional indicator symbol) |        `w`         |
|   🇽    | [U+1F1FD](https://codepoints.net/U+1F1FD) | _X_ (regional indicator symbol) |        `x`         |
|   🇾    | [U+1F1FE](https://codepoints.net/U+1F1FE) | _Y_ (regional indicator symbol) |        `y`         |
|   🇿    | [U+1F1FF](https://codepoints.net/U+1F1FF) | _Z_ (regional indicator symbol) |        `z`         |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Keyboards](#keyboards) | [Flags](#flags) ⬆️

### Common

#### Cards

Symbols representing cards and card suits.

| Symbol |                 Unicode                 | Description | Hotstring / hotkey |
| :----: | :-------------------------------------: | :---------: | :----------------: |
|   ♠    | [U+2660](https://codepoints.net/U+2660) |   spades    |     `spades\`      |
|   ♣    | [U+2663](https://codepoints.net/U+2663) |    clubs    |      `clubs\`      |
|   ♥    | [U+2665](https://codepoints.net/U+2665) |   hearts    |     `hearts\`      |
|   ♦    | [U+2666](https://codepoints.net/U+2666) |  diamonds   |    `diamonds\`     |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Cards](#cards) ⬆️

#### Diacritics

Combining diacritical marks.

| Symbol |                 Unicode                 |  Description   |    Hotstring / hotkey     |
| :----: | :-------------------------------------: | :------------: | :-----------------------: |
|   ◌̀   | [U+0300](https://codepoints.net/U+0300) |     grave      |      `Alt` + `` ` ``      |
|   ◌́   | [U+0301](https://codepoints.net/U+0301) |     acute      |        `Alt` + `'`        |
|   ◌̂   | [U+0302](https://codepoints.net/U+0302) |   circumflex   |        `Alt` + `6`        |
|   ◌̃   | [U+0303](https://codepoints.net/U+0303) |     tilde      |        `Alt` + `1`        |
|   ◌̄   | [U+0304](https://codepoints.net/U+0304) |     macron     |        `Alt` + `-`        |
|   ◌̆   | [U+0306](https://codepoints.net/U+0306) |     breve      |        `Alt` + `5`        |
|   ◌̈   | [U+0308](https://codepoints.net/U+0308) |   diaeresis    |        `Alt` + `;`        |
|   ◌̊   | [U+030A](https://codepoints.net/U+030A) |    overring    |        `Alt` + `0`        |
|   ◌̋   | [U+030B](https://codepoints.net/U+030B) | double accute  |   `Alt` + `Shift` + `'`   |
|   ◌̌   | [U+030C](https://codepoints.net/U+030C) |     caron      |        `Alt` + `7`        |
|   ◌̏   | [U+030F](https://codepoints.net/U+030F) |  double grave  | `Alt` + `Shift` + `` ` `` |
|   ◌̑   | [U+0311](https://codepoints.net/U+0311) | inverted breve |        `Alt` + `4`        |
|   ◌̧   | [U+0327](https://codepoints.net/U+0327) |    cedilla     |        `Alt` + `,`        |
|   ◌̨   | [U+0328](https://codepoints.net/U+0328) |     ogonek     |        `Alt` + `.`        |
|   ◌    | [U+25CC](https://codepoints.net/U+25CC) | dotted circle  |         `circle\`         |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Diacritics](#diacritics) ⬆️

#### Letters

Miscellaneous letters.

| Symbol | Uppercase |                                      Unicode                                      |       Description        | Hotstring / hotkey |
| :----: | :-------: | :-------------------------------------------------------------------------------: | :----------------------: | :----------------: |
|   œ    |     Œ     | [U+0153](https://codepoints.net/U+0153) / [U+0152](https://codepoints.net/U+0152) |           _oe_           |   `oe\` / `OE\`    |
|   ʾ    |           |                      [U+02BE](https://codepoints.net/U+02BE)                      | letter half ring (right) |       `''\`        |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Letters](#letters) ⬆️

#### Logic

Symbols used in mathematical logic.

| Symbol |                 Unicode                 |         Description         | Hotstring / hotkey |
| :----: | :-------------------------------------: | :-------------------------: | :----------------: |
|   ¬    | [U+00AC](https://codepoints.net/U+00AC) |  negation (logical _NOT_)   |       `not\`       |
|   ∧    | [U+2227](https://codepoints.net/U+2227) | conjunction (logical _AND_) |       `and\`       |
|   ∨    | [U+2228](https://codepoints.net/U+2228) | disjunction (logical _OR_)  |       `or\`        |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Logic](#logic) ⬆️

#### Mathematics

Various mathematical symbols.

| Symbol |                 Unicode                 |     Description     | Hotstring / hotkey |
| :----: | :-------------------------------------: | :-----------------: | :----------------: |
|   ±    | [U+00B1](https://codepoints.net/U+00B1) |     plus minus      |       `+-\`        |
|   ×    | [U+00D7](https://codepoints.net/U+00D7) | multiplication sign |        `x\`        |
|   ∅    | [U+2205](https://codepoints.net/U+2205) |      empty set      |      `empty\`      |
|   ∓    | [U+2213](https://codepoints.net/U+2213) |     minus plus      |       `-+\`        |
|   √    | [U+221A](https://codepoints.net/U+221A) |     square root     |      `sqrt\`       |
|   ∞    | [U+221E](https://codepoints.net/U+221E) |      infinity       |      `infty\`      |
|   ≠    | [U+2260](https://codepoints.net/U+2260) |      not equal      |       `=/=`        |
|   ≪    | [U+226A](https://codepoints.net/U+226A) |   much less than    |       `<<\`        |
|   ≫    | [U+226B](https://codepoints.net/U+226B) |  much greater than  |       `>>\`        |
|   ⋅    | [U+22C5](https://codepoints.net/U+22C5) | multiplication dot  |      `cdot\`       |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Mathematics](#mathematics) ⬆️

#### Music

Symbols used in musical notation.

| Symbol |                 Unicode                 | Description | Hotstring / hotkey |
| :----: | :-------------------------------------: | :---------: | :----------------: |
|   ♭    | [U+266D](https://codepoints.net/U+266D) |    flat     |        `b\`        |
|   ♯    | [U+266F](https://codepoints.net/U+266F) |    sharp    |        `#\`        |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Music](#music) ⬆️

#### Other

Other symbols.

| Symbol |                 Unicode                 |  Description  | Hotstring / hotkey |
| :----: | :-------------------------------------: | :-----------: | :----------------: |
|   ©    | [U+00A9](https://codepoints.net/U+00A9) |   copyright   |        `c\`        |
|   °    | [U+00B0](https://codepoints.net/U+00B0) |    degree     |       `deg\`       |
|   ™    | [U+2122](https://codepoints.net/U+2122) |   trademark   |       `tm\`        |
|   →    | [U+2192](https://codepoints.net/U+2192) | arrow (right) |       `->\`        |
|   ✓    | [U+2713](https://codepoints.net/U+2713) |  check mark   |        `v\`        |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Other](#other) ⬆️

#### Punctuation marks

Various punctuation marks.

| Symbol |                 Unicode                 |           Description            |  Hotstring / hotkey   |
| :----: | :-------------------------------------: | :------------------------------: | :-------------------: |
|   –    | [U+2013](https://codepoints.net/U+2013) |             en dash              | `Alt` + `Shift` + `=` |
|   —    | [U+2014](https://codepoints.net/U+2014) |             em dash              |      `Alt` + `=`      |
|   ”    | [U+201D](https://codepoints.net/U+201D) |  double quotation mark (right)   |         `"u\`         |
|   „    | [U+201E](https://codepoints.net/U+201E) | double low quotation mark (left) |         `"d\`         |
|   ⟨    | [U+27E8](https://codepoints.net/U+27E8) |       angle bracket (left)       | `Alt` + `Shift` + `,` |
|   ⟩    | [U+27E9](https://codepoints.net/U+27E9) |      angle bracket (right)       | `Alt` + `Shift` + `.` |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Punctuation marks](#punctuation-marks) ⬆️

#### Subscripts

Subscript characters.

| Symbol |                 Unicode                 |   Description   | Hotstring / hotkey |
| :----: | :-------------------------------------: | :-------------: | :----------------: |
|   ₀    | [U+2080](https://codepoints.net/U+2080) | _0_ (subscript) |      `sub0\`       |
|   ₁    | [U+2081](https://codepoints.net/U+2081) | _1_ (subscript) |      `sub1\`       |
|   ₂    | [U+2082](https://codepoints.net/U+2082) | _2_ (subscript) |      `sub2\`       |
|   ₃    | [U+2083](https://codepoints.net/U+2083) | _3_ (subscript) |      `sub3\`       |
|   ₄    | [U+2084](https://codepoints.net/U+2084) | _4_ (subscript) |      `sub4\`       |
|   ₅    | [U+2085](https://codepoints.net/U+2085) | _5_ (subscript) |      `sub5\`       |
|   ₆    | [U+2086](https://codepoints.net/U+2086) | _6_ (subscript) |      `sub6\`       |
|   ₇    | [U+2087](https://codepoints.net/U+2087) | _7_ (subscript) |      `sub7\`       |
|   ₈    | [U+2088](https://codepoints.net/U+2088) | _8_ (subscript) |      `sub8\`       |
|   ₉    | [U+2089](https://codepoints.net/U+2089) | _9_ (subscript) |      `sub9\`       |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Subscripts](#subscripts) ⬆️

#### Superscripts

Superscript characters.

| Symbol |                 Unicode                 |    Description    | Hotstring / hotkey |
| :----: | :-------------------------------------: | :---------------: | :----------------: |
|   ²    | [U+00B2](https://codepoints.net/U+00B2) | _2_ (superscript) |      `sup2\`       |
|   ³    | [U+00B3](https://codepoints.net/U+00B3) | _3_ (superscript) |      `sup3\`       |
|   ¹    | [U+00B9](https://codepoints.net/U+00B9) | _1_ (superscript) |      `sup1\`       |
|   ⁰    | [U+2070](https://codepoints.net/U+2070) | _0_ (superscript) |      `sup0\`       |
|   ⁴    | [U+2074](https://codepoints.net/U+2074) | _4_ (superscript) |      `sup4\`       |
|   ⁵    | [U+2075](https://codepoints.net/U+2075) | _5_ (superscript) |      `sup5\`       |
|   ⁶    | [U+2076](https://codepoints.net/U+2076) | _6_ (superscript) |      `sup6\`       |
|   ⁷    | [U+2077](https://codepoints.net/U+2077) | _7_ (superscript) |      `sup7\`       |
|   ⁸    | [U+2078](https://codepoints.net/U+2078) | _8_ (superscript) |      `sup8\`       |
|   ⁹    | [U+2079](https://codepoints.net/U+2079) | _9_ (superscript) |      `sup9\`       |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Superscripts](#superscripts) ⬆️

#### Zodiac

Western zodiac signs.

| Symbol |                 Unicode                 | Description | Hotstring / hotkey |
| :----: | :-------------------------------------: | :---------: | :----------------: |
|   ♈    | [U+2648](https://codepoints.net/U+2648) |    Aries    |      `aries\`      |
|   ♉    | [U+2649](https://codepoints.net/U+2649) |   Taurus    |     `taurus\`      |
|   ♊    | [U+264A](https://codepoints.net/U+264A) |   Gemini    |     `gemini\`      |
|   ♋    | [U+264B](https://codepoints.net/U+264B) |   Cancer    |     `cancer\`      |
|   ♌    | [U+264C](https://codepoints.net/U+264C) |     Leo     |       `leo\`       |
|   ♍    | [U+264D](https://codepoints.net/U+264D) |    Virgo    |      `virgo\`      |
|   ♎    | [U+264E](https://codepoints.net/U+264E) |    Libra    |      `libra\`      |
|   ♏    | [U+264F](https://codepoints.net/U+264F) |   Scorpio   |    `scorpius\`     |
|   ♐    | [U+2650](https://codepoints.net/U+2650) | Sagittarius |   `sagittarius\`   |
|   ♑    | [U+2651](https://codepoints.net/U+2651) |  Capricorn  |    `capricorn\`    |
|   ♒    | [U+2652](https://codepoints.net/U+2652) |  Aquarius   |    `aquarius\`     |
|   ♓    | [U+2653](https://codepoints.net/U+2653) |   Pisces    |     `pisces\`      |

⬆️ go back to [top](#multilingual-keyboard) | [Hotkeys & hotstrings](#hotkeys--hotstrings) | [Common](#common) | [Zodiac](#zodiac) ⬆️
