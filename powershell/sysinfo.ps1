#$Hello = "Hello, powershell!"
#write-host($Hello)
function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

Write-Host(getIP)
$IP = getIP
Write-Host("This machines IP is $IP")
Write-Host("This machine's IP is {0}" -f $IP)

$DATE = Get-date
$version = $host.version.Major
$Body = "This machine's IP is $IP. User is $env:USERNAME. Hostname is $env:COMPUTERNAME. Powershell version is $version. Today's date is $DATE"

write-host($body)

#Send-MailMessage -to "jones6ju@mail.uc.edu" -from "justinjonesmtmm@gmail.com" -subject "IT3038c windows SysInfo" -body $Body -smtpserver smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)