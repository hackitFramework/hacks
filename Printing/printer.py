import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def select():
    filePath = askopenfilename()
    h = hostname.get()
    p = port.get()
    output = "cat '" + str(filePath) + "' | netcat -h " + h + " -p " + p
    print(output)

#window making
window = Tk()
window.title("Path Printer")
window.geometry("200x100")

#entry fields
tk.Label(window, text="hostname").grid(row=0)
tk.Label(window, text="port").grid(row=1)

hostname = tk.Entry(window, text="hostname")
port = tk.Entry(window, text="port")
hostname.grid(row=0, column=1, columnspan=4, pady=10, padx=5, sticky=tk.W)
port.grid(row=1, column=1, columnspan=4, padx=5, sticky=tk.W)

#button
button = tk.Button(window, text='Get Path', command=select, fg='Black', bg='#0ddabb')
button.grid(row=3, column=1, columnspan=4, padx=10, pady=5)

window.mainloop()
