$ver = Read-Host "Please enter your version in format YY.0M.MICRO (CalVer)"

Write-Output "`n`n==================== Start build ====================`n`n"

flet pack --icon favico.ico --name QuickTest --product-name QuickTest --product-version $ver --file-version $ver --copyright "https://stepik.org/course/179843/promo" --onedir main.py
iscc /dMyAppVersion=$ver pack_to_setup.iss

Write-Output "`n`n==================== Build Done ====================`n`n"