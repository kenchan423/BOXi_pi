import RPi.GPIO as GPIO
import time

vib = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(vib,GPIO.IN)

while True:
    reading = GPIO.input(vib)
    if reading: 
        print("ALARM")
    else:
        print("Normal")
    time.sleep(0.1)