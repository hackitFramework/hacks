#
# hsamuelson
#
# Playing around with keyboard an os.system()

# Calls itself (py) from within a command terminal inside of its self.
#   Seems to max out at 61 nested sessions. with 'python' not found. 

import keyboard
import sys
inVar = (sys.argv[1])
print(inVar)
#keyboard.press("CTRL+Z")
#keyboard.release("CTRL+Z")
#keyboard.press("ENTER")
#keyboard.release("ENTER")
import os
#keyboard.release()
os.system(str("python keyJump.py" + " " +str(1+int(inVar))))