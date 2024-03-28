@echo off
echo Running Part Two...
echo.

echo 1. Installing Windows 11 Pro product key...
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
echo.

echo 2. Setting KMS server...
slmgr /skms kms8.msguides.com
echo.

echo 3. Activating Windows...
slmgr /ato
echo.

echo You should now have Windows 11 Pro. I would suggest restarting your PC, but it is not needed.
echo.
exit
