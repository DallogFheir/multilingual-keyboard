; DEFAULT
#NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
; (DISABLED) SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.

; AUTO-EXECUTE SECTION
keyboard := "default"
curIcon := "default"
Menu, Tray, Icon, icons\language_specific\default.ico

; * = without ending char, ? = inside another string
#Hotstring * ?

; input level above precomposed characters
#InputLevel, 1

; VARIABLES
!+1::
    keyboard := "default"
    curIcon := "default"
    Menu, Tray, Icon, icons\language_specific\default.ico
return

!+2::
    keyboard := "cyrillic"
    curIcon := "cyrillic"
    Menu, Tray, Icon, icons\language_specific\cyrillic.ico
return

!+3::
    keyboard := "greek"
    curIcon := "greek"
    Menu, Tray, Icon, icons\language_specific\greek.ico
return

!+4::
    keyboard := "ipa"
    curIcon := "ipa"
    Menu, Tray, Icon, icons\language_specific\ipa.ico
return

!+5::
    keyboard := "flag"
    curIcon := "flag"
    Menu, Tray, Icon, icons\language_specific\flag.ico
return

; INTERNATIONAL KEYBOARD
#Hotstring C
#If keyboard = "default"
    #include subscripts\keyboards\default.ahk
#If

#If keyboard = "cyrillic"
    #include subscripts\keyboards\cyrillic.ahk
#If

#If keyboard = "greek"
    #include subscripts\keyboards\greek.ahk
#If

#If keyboard = "ipa"
    #include subscripts\keyboards\ipa.ahk
#If

#If keyboard = "flag"
    #include subscripts\keyboards\flag.ahk
#If

#Hotstring C0

; COMMON
#include subscripts\common.ahk
; PRECOMPOSED_CHARACTERS
#include subscripts\precomposed_characters.ahk
; UTILS
#include subscripts\utils.ahk
