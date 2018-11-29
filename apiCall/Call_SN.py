#!/usr/bin/python
import requests
class CallCloud:
    def callServiceNow(self):
        print('Calling to Servicenow')
        url = 'https://benchmarkskingston.service-now.com/api/sn_hack_iot_centra/iot_api/send_signal'
        payload = "{'device_id' : '1234'}"
        headers = {'content-type':'application/json'}
        response = requests.post(url, data=payload, headers=headers, auth=('admin','admin'))
        print(response.status_code)
        return "200"
    def registerServiceNow(self):
        print('Registering to Servicenow')
        url = 'https://benchmarkskingston.service-now.com/api/sn_hack_iot_centra/iot_api/send_signal'
        payload = "{'device_id' : '1234'}"
        headers = {'content-type':'application/json'}
        response = requests.post(url, data=payload, headers=headers, auth=('admin','admin'))
        print(response.status_code)
        return "200"
   
if __name__== "__main__":
   CallCloud().callServiceNow()
