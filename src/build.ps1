$ver = Read-Host "Please enter your version in format YY.0M.MICRO (CalVer)"
$repo_path = Split-Path $PWD

$InstallerLocation = $repo_path
$InstallerIcon = $repo_path + "\src\favico.ico"
$Source_exe_Location = $repo_path + "\src\dist\QuickTest\QuickTest.exe"
$Source_other = $repo_path + "\src\dist\QuickTest\*"
$LicenseLocation = $repo_path + "\LICENSE"

Write-Output "`n"$InstallerLocation $InstallerIcon $Source_exe_Location $Source_other $LicenseLocation

Write-Output "`n`n==================== Start build and pack ====================`n`n"

flet pack --icon favico.ico `
    --name QuickTest `
    --product-name QuickTest `
    --product-version $ver `
    --file-version $ver `
    --copyright "https://stepik.org/course/179843/promo" `
    --onedir main.py

iscc /dMyAppVersion=$ver `
    /dInstallerLocation=$InstallerLocation `
    /dInstallerIcon=$InstallerIcon `
    /dSource_exe_Location=$Source_exe_Location `
    /dSource_other=$Source_other `
    /dLicenseLocation=$LicenseLocation pack_to_setup.iss

Write-Output "`n`n==================== Build and pack done ====================`n`n"