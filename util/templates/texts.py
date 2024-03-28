INTRO = """<img src="./logo.png" alt="Multilingual Keyboard" width="60px" />

**Multilingual Keyboard** is an Autohotkey application that allows you to easily \
switch between keyboard layouts of different languages and scripts, and provides \
hotstrings for a variety of symbols.

## Usage

To use this app, you have to install [AutoHotkey](https://www.autohotkey.com/)
and download the release from this repository. Then you can just run
the `main.ahk` file.

The app currently supports 5 keyboard layouts:

1. **default**, containing a variety of common-use symbols, but not modifying any standard keys
2. **Cyrillic**, containing the letters of the Cyrillic alphabet
3. **Greek**, containing the letters of the Greek alphabet
4. **IPA**, containing the symbols of the International Phonetic Alphabet
5. **flag**, containing the _regional indicator symbols_ used to produce flag emojis

You can switch between keyboards by pressing `AltGr` + `Shift` + the keyboard's number, for example `AltGr` + `Shift` + `5` for the flag keyboard.

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

"""

OUTRO = """
## Acknowledgements

The base for the logo created by [Gregor Cresnar - Flaticon](https://www.flaticon.com).
"""
