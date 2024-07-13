; DEFAULT
#SingleInstance Force

; AUTO-EXECUTE SECTION
{AUTO_EXECUTE_SECTION}

; * = without ending char
; ? = inside another string
; C = case-sensitive
#Hotstring * ? C

; input level above precomposed characters
#InputLevel 1

; KEYBOARD LAYOUTS
; hotkeys
{HOTKEYS}

; switches
{IF_STATEMENTS}

; includes
#include common.ahk
#include precomposed_characters.ahk
#include utils.ahk
