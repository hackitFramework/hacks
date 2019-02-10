using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Text; 
using System.Threading.Tasks; 
using System.Drawing; 
using System.IO;
using System.Windows.Forms;
using System.Runtime.InteropServices;



namespace Test_Application_C_Sharp 
{ 
    class Program 
    {
        // Activate Console Window
        [DllImport("user32.dll")]
        public static extern IntPtr FindWindow(string lpClassName, string lpWindowName);
        
        // Hide or show
        [DllImport("user32.dll")]
        static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

        static void Main(string[] args) 
        {
            IntPtr hWnd = FindWindow(null, System.Windows.Forms.Application.ExecutablePath);
            ShowWindow(hWnd, 0);

            // Setting up image container
            Bitmap memoryImage;
            memoryImage = new Bitmap(1920, 1080); 
            Size s = new Size(memoryImage.Width, memoryImage.Height); 
  
            // Getting screen
            Graphics memoryGraphics = Graphics.FromImage(memoryImage); 
            memoryGraphics.CopyFromScreen(0, 0, 0, 0, s); 
 
            // Save image 
            string str = ""; 
            try 
            { 
                str = string.Format(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments) + 
                      @"\Screenshot.png"); 
            }
            catch (Exception er)
            {
                Console.WriteLine("Sorry, there was an error: " + er.Message);
                Console.WriteLine();
            }
            memoryImage.Save(str);
        }
    }
}