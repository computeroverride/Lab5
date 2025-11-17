from hal import hal_led as led
from threading import Thread
from time import sleep
from hal import hal_keypad as keypad

def led_thread(): 
    global delay 
    while(True): 
        if delay != 0: 
            led.set_output(20,1) 
            sleep(delay) 
            led.set_output(20, 0) 
            sleep(delay)
        else:
            break
            
def led_control_init(): 
    led.init()
    global delay 
    delay=1
    t1 = Thread(target=led_thread) 
    t1.start() 
    #Set initial LED blinking every 1 second after Thread starts  

    led.init()
    
def setdelay(a):
    global delay
    delay = a