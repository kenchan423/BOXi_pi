import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

try:
    hx = HX711(
        dout_pin=5,
        pd_sck_pin=6#,
        #channel='A',
        #gain=64
    )
    
    hx.reset()
    
    print("Performing Tare.  Remove items from scale.")
    time.sleep(1)
    
    cals = hx.get_raw_data(times=3)
    print(str(cals))
    offset = -1*(cals[0]+cals[1]+cals[2])/3
    print(str(offset))
    
    print("Tare complete. Place laptop for calibration.")
    time.sleep(5)
    
    measures = hx.get_raw_data(times=3)
    w = (measures[0]+measures[1]+measures[2])/3
    #measures[0] = measures[0] + offset
    #measures[1] = measures[1] + offset
    #measures[2] = measures[2] + offset
    ratio = (w + offset) / 1632.932532
    print(str(ratio))
    
    print("Calibration complete. Try weighing something.")
    time.sleep(7)
    
    data = hx.get_raw_data(times=3)
    print(str(data))
    avg = ((data[0]+data[1]+data[2])/3 + offset)/ratio
    
    
finally:
    GPIO.cleanup()
    print(str(avg))