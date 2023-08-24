; DEFAULT
#NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
; (DISABLED) SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
; SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.
#SingleInstance Force

; AUTO-EXECUTE SECTION
keyboard := "default"
curIcon := "default"
Menu, Tray, Icon, icons\keyboards\default.ico

; * = without ending char
; ? = inside another string
; C = case-sensitive
#Hotstring * ? C

; input level above precomposed characters
#InputLevel, 1

; KEYBOARD LAYOUTS
; hotkeys
!+1::
    keyboard := "default"
    curIcon := "default"
    Menu, Tray, Icon, icons\keyboards\default.ico
return

!+2::
    keyboard := "cyrillic"
    curIcon := "cyrillic"
    Menu, Tray, Icon, icons\keyboards\cyrillic.ico
return

!+3::
    keyboard := "greek"
    curIcon := "greek"
    Menu, Tray, Icon, icons\keyboards\greek.ico
return

!+4::
    keyboard := "ipa"
    curIcon := "ipa"
    Menu, Tray, Icon, icons\keyboards\ipa.ico
return

!+5::
    keyboard := "flag"
    curIcon := "flag"
    Menu, Tray, Icon, icons\keyboards\flag.ico
return

; switches
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

; COMMON
#include subscripts\common.ahk
; PRECOMPOSED_CHARACTERS
#include subscripts\precomposed_characters.ahk
; UTILS
#include subscripts\utils.ahk
