# change import lines later
import scan_barcode as waveshare
import open_sesame
import 

# reading in barcodes
tracking_number = waveshare.readData()
print(tracking_number)

# trip relay & open lock
open_sesame.trip()

"""
import RPi.GPIO as GPIO
import time

# Disable warnings
GPIO.setwarnings(False)  

# RELAY & LOCK
# Set up GPIO pins for relay & lock
GPIO.setmode(GPIO.BOARD)

lock_trip = 36
GPIO.setup(lock_trip, GPIO.OUT)

vib = 36
GPIO.setup(vib,GPIO.IN)

# import trip function
from BOXi_pi.lock import trip

# BARCODE SCANNER
import serial

# import barcode scanning feature
import barcode_scanner.scan_barcode as waveshare

from vibration.vibration_sensor import vib

from hx711 import HX711
from weight_sensor.weigh import job
# always scanning for barcodes, checking weight and vibration

# i dunno if i should put a while loop or an if statement?
# tracking_number = waveshare.scan()
# if barcode scanned
    # then print tracking number (later on verifying tracking number)
    # & open the lock
    print(tracking_number)
    time.sleep(0.5)
    
    print("Tracking number valid.")
    time.sleep(0.5)
    
    print("Opening lock in 3...")
    time.sleep(3)
    trip()

"""




