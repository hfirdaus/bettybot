#Declare Variables
$SearchDirectory = "C:\Users\dtmacroh\Dropbox\IFTTT"
$SleepTime = 5

Do {
Start-Sleep -Seconds $SleepTime
$FileCheck = Test-Path -Path "$SearchDirectory\runRobot.txt"
}
Until ($FileCheck -eq $True)

Remove-Item -Path "$SearchDirectory\runRobot.txt"

$cmdPath = “C:\Program Files\MobileRobots\ARIA\bin64\bettybot.exe"
$cmdArgList = @("-rp", "COM4")

& $cmdPath $cmdArgList