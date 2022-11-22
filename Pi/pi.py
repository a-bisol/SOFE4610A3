import RPi.GPIO as GPIO
import time

readPIN = 14
ledPIN = 3
ledON = False
dark = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(readPIN, GPIO.IN)
GPIO.setup(ledPIN, GPIO.OUT)
GPIO.setwarnings(True)


while True:
    #check state of resistor - transmit to API endpoint
    if (GPIO.input(readPIN)==1):
        dark = True
    else:
        dark = False
        
    #placeholder to switch state - get from API endpoint later
    if (dark):
        ledON = True
    else:
        ledON = False
        
    #if ledON is enabled then turn on light    
    if (ledON):
        GPIO.output(ledPIN, GPIO.HIGH)
    else:
        GPIO.output(ledPIN, GPIO.LOW)
    
    print("Dark: "+str(dark)+" LED: "+str(ledON))
    time.sleep(2)
