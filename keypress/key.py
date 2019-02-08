import keyboard
import time
import os

# 1 = speech; 2 = sound file
mode = 2

#for i in range(1,100000):
while True:
    while True:
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    #print('You Pressed A Key!')
                    if(mode == 1):
                        os.system("keypres.vbs")
                    elif(mode == 2):
                        os.system("sound.vbs")
                    time.sleep(2)
                    break  # finishing the loop
                else:
                    pass
            except:
                pass
