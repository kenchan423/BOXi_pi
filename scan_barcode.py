import serial
import json
import requests
#from time import sleep

ser = serial.Serial('/dev/ttyS0', 9600)

#def setup():
    
#, timeout=5,parity=serial.PARITY_ODD
def readData():
    buffer = ""
    while True:
        oneByte = ser.read(1)
        if oneByte == b"\r":
            return buffer
        else:
            buffer += oneByte.decode("ascii")
ind = 0

def send_to_server():
    while True:
        barcode = readData()
        ind += 1
        barcode_dict = dict({ind:barcode})
        #print(barcode_dict)
        #with open("barcodes.json", "a") as outfile:
        #    json.dump(barcode_dict, outfile)
        
        r = requests.post('https://httpbin.org/post', json=barcode_dict, verify=False)
        print(f"Status Code: {r.status_code}, Response: {r.json()}")
        #r = requests.get('http
        #recieved_data = ser.read()
        
        #sleep(0.03)
        #data_left = ser.inWaiting()
        #recieved_data = ser.read(data_left)
        #print('Reading data')
        #print(recieved_data)
        #ser.write(recieved_data)
        
def scan():
    barcode = readData()
    return barcode



def cleanup():
    ser.close()

def __init__():
    return True
