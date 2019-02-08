import keyboard
import time
import os
#for i in range(1,100000):
while True:
    while True:
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    #print('You Pressed A Key!')
                    os.system("keypres.vbs")
                    time.sleep(2)
                    break  # finishing the loop
                else:
                    pass
            except:
                pass