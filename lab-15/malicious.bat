@echo off
set "fileToDelete=/home/mansij/Desktop/important.txt"
if exist "%fileToDelete%" (
 del "%fileToDelete%"
 echo File deleted successfully.
) else (
 echo The file does not exist or the path is incorrect.
)
pause