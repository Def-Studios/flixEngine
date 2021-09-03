@echo off
set /p id="name: "
robocopy "new flix project" %id% /E
cd %id%
rename game.exe %id%.exe
