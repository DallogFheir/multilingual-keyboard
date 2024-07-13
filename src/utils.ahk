#SuspendExempt
F2::
{
    iconPath := curIcon == "*" ? "*" : "icons\keyboards\" curIcon ".ico"

    if A_IsSuspended
    {
        TraySetIcon %iconPath%, 0
    }
    else
    {
        TraySetIcon "icons\suspend.ico", , 1
    }
    Suspend -1
}
#SuspendExempt False

; disables changing languages on Windows
#Space::
{ }