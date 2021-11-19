import RPi.GPIO as GPIO
import time

lock_trip = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lock_trip, GPIO.OUT)

GPIO.output(lock_trip, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(lock_trip, GPIO.LOW)