import requests

def getResponse(zvmUrl, endPoint, inputHeaders):
    return requests.get(zvmUrl + endPoint, headers=inputHeaders, verify=False)

def putResponse(zvmUrl, endPoint, inputHeaders, body):
    return requests.put(zvmUrl + endPoint, data=body, headers=inputHeaders, verify=False)

def deleteResponse(zvmUrl, endPoint, inputHeaders):
    return requests.delete(zvmUrl + endPoint, headers=inputHeaders, verify=False)

def postResponse(zvmUrl, endPoint, inputHeaders, body):
    return requests.post(zvmUrl + endPoint, data=body, headers=inputHeaders, verify=False)