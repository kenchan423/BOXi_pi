import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

def job():

    GPIO.setmode(GPIO.BCM)
    offset = 217653
    ratio = 6

    try:
        hx = HX711(
            dout_pin=5,
            pd_sck_pin=6#,
            #channel='A',
            #gain=64
        )
        
        hx.reset()
        data = hx.get_raw_data(times=3)
        avg = ((data[0]+data[1]+data[2])/3 + offset)/ratio
        kg = avg/1000
        
    finally:
        GPIO.cleanup()
        print("Item weighs " + str(kg) + " kg")
        return kg

if __name__ == '__main__':
    job()