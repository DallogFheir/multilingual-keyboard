; DEFAULT
#NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
; (DISABLED) SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
; SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.
#SingleInstance Force

; AUTO-EXECUTE SECTION
{AUTO_EXECUTE_SECTION}

; * = without ending char
; ? = inside another string
; C = case-sensitive
#Hotstring * ? C

; input level above precomposed characters
#InputLevel, 1

; KEYBOARD LAYOUTS
; hotkeys
{HOTKEYS}

; switches
{IF_STATEMENTS}

; COMMON
#include subscripts\common.ahk
; PRECOMPOSED_CHARACTERS
#include subscripts\precomposed_characters.ahk
; UTILS
#include subscripts\utils.ahk
