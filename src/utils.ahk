; suspends this script
F2::
    suspend, Permit

    iconPath := curIcon == "*" ? "*" : "icons\keyboards\" curIcon ".ico"

    if A_IsSuspended
    {
        Menu, Tray, Icon, %iconPath% , 0
        Suspend, Off
    }
    else
    {
        Menu, Tray, Icon, icons\suspend.ico, , 1
        Suspend, On
    }
return

; disables changing languages
#Space::
return
