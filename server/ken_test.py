import json
import requests

def run():
    barcode = 'asdf'
    ind = 0
    # barcode_dict = dict({ind:barcode})
    server_url = 'http://155.41.26.248:3000'
    payload = {"userId": "Yd7AB4stMMRkoUz8uh5Vw4xKtFr1","trackingNumber": "TBA089957395104"}
    
    r = requests.post(f'{server_url}/package', json=payload)
    print(f"Status Code: {r.status_code}, Response: {r.text}")
    #https://httpbin.org/post
    
        #r = requests.get('http
        #recieved_data = ser.read()
        
        #sleep(0.03)
        #data_left = ser.inWaiting()
        #recieved_data = ser.read(data_left)
        #print('Reading data')
        #print(recieved_data)
        #ser.write(recieved_data)

# always looking to scan
#
if __name__ == "__main__":
    run()