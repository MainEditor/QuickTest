$ver = Read-Host "Please enter your version in format YY.0M.MICRO (CalVer)"

Write-Output "-------------------------------------------Start build-------------------------------------------"

flet pack --icon favico.ico --name QuickTest.exe --product-name QuickTest --product-version $ver --file-version $ver --copyright "https://stepik.org/course/179843/promo" main.py

Write-Output "-------------------------------------------Build Done--------------------------------------------`n`n"

Write-Output "Checking is .exe file already exist and deleting if it exist"

$path = "$env:USERPROFILE\Desktop\QuickTest.exe"

if (Test-Path $path) {
    Remove-Item $path
}

Write-Output "Moving new .exe file to \Desktop"
Move-Item $PWD"\dist\QuickTest.exe" "$ENV:USERPROFILE\Desktop"

Write-Output "Deleting \build folder"
Remove-Item $PWD"\build" -Recurse

Write-Output "Deleting .spec file"
Remove-Item $PWD"\QuickTest.exe.spec"

Write-Output "Deleting \dist folder"
Remove-Item $PWD"\dist"

Write-Output "              DONE!               "