import RPi.GPIO as GPIO
import time

readPIN = 14
ledPIN = 18
state = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(readPIN, GPIO.IN)
GPIO.setup(ledPIN, GPIO.OUT)
GPIO.setwarnings(True)

print(" Read: " + str(GPIO.input(readPIN)))
time.sleep(1)

if state:
    GPIO.output(ledPIN,GPIO.HIGH)
else:
    GPIO.output(ledPIN,GPIO.LOW)
