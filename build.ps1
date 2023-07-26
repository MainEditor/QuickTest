$ver = Read-Host "Please enter your version in format YY.0M.MICRO (CalVer)"

flet pack --icon favico2.ico --name QuickTest.exe --product-name QuickTest --product-version $ver --file-version $ver --copyright "https://stepik.org/course/179843/promo" main.py

$path = "$env:USERPROFILE\Desktop\QuickTest.exe"

if (Test-Path $path) {
    Remove-Item $path
}

Move-Item $PWD"\dist\QuickTest.exe" "$ENV:USERPROFILE\Desktop"

Remove-Item $PWD"\build" -Recurse

Remove-Item $PWD"\QuickTest.exe.spec"

Remove-Item $PWD"\dist"
