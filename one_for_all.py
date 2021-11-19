import RPi.GPIO as GPIO
import time

# Disable warnings
GPIO.setwarnings(False)

# RELAY & LOCK
# Set up GPIO pins for relay & lock
GPIO.setmode(GPIO.BOARD)

lock_trip = 36

GPIO.setup(lock_trip, GPIO.OUT)

# import trip function
from BOXi_pi.lock import trip

# BARCODE SCANNER
import serial

ser = serial.Serial('/dev/ttyS0', 9600)

# import barcode scanning feature
import scan_barcode as waveshare




