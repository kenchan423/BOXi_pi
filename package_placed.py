import time
import sys

#sys.path.insert(0, '/home/pi/desktop')
sys.path.insert(0, '/home/pi/hx711py')

#from .weigh import job
#import weigh
import calibration.py as  cal
#Startup condition

#last_weight = weigh.job()

#while True:
 #   new_weight = weigh.job()
 #   if (new_weight - last_weight)>0.1:
 #       print("Package placed")
 #   last_weight = new_weight
 #   time.sleep(0.5)
 
#mod.cleanAndExit()
#mod.setup()
#mod.loop()
 
cal.setup()
cal.calibrate()