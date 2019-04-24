#
# fReE pRiNtEr
#
# vKnife 
# Henry Samuelson, Christopher Hansen

# Get free printing on any of Cornell University printers
#



# linux command 
#cat you_file.prn | netcat -w 1 printer_ip 9100
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import nmap


Tk().withdraw() 
filename = askopenfilename()
#print(filename)



command1 = "cat " + str(filename) + " | netcat -w 1 " + str(printerIP) + "9100"


