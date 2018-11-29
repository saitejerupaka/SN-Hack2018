import RPi.GPIO as GPIO
from Call_SN import CallCloud
import time
def Main():
    callCloud = CallCloud()	
    GPIO.setmode(GPIO.BCM)
    led = 24
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO17
    GPIO.setup(led, GPIO.OUT)  #LED to GPIO24
    try:
        print('Program Started.. Listening Signal')
        while True:
            button_state = GPIO.input(17)
            if button_state == False:
                GPIO.output(led, GPIO.HIGH)
                print('Button Pressed...')
                print(callCloud.callServiceNow())
                time.sleep(0.2)
            else:
                GPIO.output(led, GPIO.LOW)
    except:
        GPIO.cleanup()
Main()
