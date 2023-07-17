; suspends this script
F2::
    suspend, Permit
    if A_IsSuspended
    {
        Menu, Tray, Icon, icons\keyboards\%curIcon%.ico, , 0
        Suspend, Off
    }
    else
    {
        Menu, Tray, Icon, icons\suspend.ico, , 1
        Suspend, On
    }
return

#Space::
return