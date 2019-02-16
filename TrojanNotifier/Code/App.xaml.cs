using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using System.Drawing;

namespace Screenshot
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
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

            System.Windows.Application.Current.Shutdown();
        }
    }
}
