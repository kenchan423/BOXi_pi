import time
import sys

sys.path.insert(1, '/home/pi/desktop')
#sys.path.insert(0, '/home/pi/hx711py')

import scan_barcode as waveshare
import open_sesame



#waveshare.setup()
tracking_number = waveshare.scan()
waveshare.cleanup()

print(tracking_number)
time.sleep(0.5)
print("Tracking number valid.")
time.sleep(0.5)
print("Opening lock in 3...")
time.sleep(3)

open_sesame.trip()