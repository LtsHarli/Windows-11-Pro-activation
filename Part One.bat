@echo off
echo Running Part One...
echo.

echo 1. Removing current product key...
cscript //nologo %windir%\system32\slmgr.vbs /upk
echo.

echo 2. Clearing product key from registry...
cscript //nologo %windir%\system32\slmgr.vbs /cpky
echo.

echo 3. Clearing KMS server...
cscript //nologo %windir%\system32\slmgr.vbs /ckms
echo.

echo 4. Getting target editions...
Dism /online /Get-TargetEditions
echo.

echo 5. Starting License Manager service...
sc config LicenseManager start= auto
net start LicenseManager
echo.

echo 6. Starting Windows Update service...
sc config wuauserv start= auto
net start wuauserv
echo.

echo 7. Changing product key...
changepk.exe /productkey VK7JG-NPHTM-C97JM-9MPGT-3V66T
echo.

echo Part one is now finished. Please restart the computer and run part two.
echo This will give you 15s to read that message; PLEASE DO NOT EXIT THE SCRIPT YET!
ping 127.0.0.1 -n 16 > nul
exit
