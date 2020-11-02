import json
import requests

def addLicense(headerwithkey, zvm_url, licenseKey):

    endPoint = '/license'
    response = requests.put(zvm_url + endPoint, data=json.dumps({"LicenseKey": licenseKey}), headers=headerwithkey, verify=False)
    print(response)

def delLicense(headerwithkey, zvm_url):

    endPoint = '/license'
    response = requests.delete(zvm_url + endPoint, headers=headerwithkey, verify=False)
    print(response)