$ver = Read-Host "Please enter your version in format YY.0M.MICRO (CalVer)"

Write-Output "-------------------------------------------Start build-------------------------------------------"

flet pack --icon favico.ico --name QuickTest --product-name QuickTest --product-version $ver --file-version $ver --copyright "https://stepik.org/course/179843/promo" --onedir main.py

Write-Output "-------------------------------------------Build Done--------------------------------------------`n`n"