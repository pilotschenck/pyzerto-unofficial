import json
import requests
import crudFunctions

class alerts():
    """The alerts API returns information about alerts and dismisses or undismisses a specific alert.

    ...

    Attributes
    ----------
    zvmurl : str
        full path to the target Zerto Virtual Manager API endpoint, e.g. 'https://10.0.1.20:9669/v1'
    headerwithkey : dict
        python dict object with the required REST headers, including a valid session key.
    alertid : str
        optional attribute specifying a specific alertId. Default is None.

    Methods
    -------
    infoAllAlerts()
        Get info on all alerts.
    """
    endPoint = '/alerts'

    def __init__(self, zvmurl, headerwithkey, alertid=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.alertid = alertid

    def infoAllAlerts(self):

        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response)
        return response

    def infoSingleAlert(self, alertid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + str(alertid), headers=self.headerwithkey, verify=False)
        print(response)
        return response

    def validAlertEntitiesValues(self):

        response = requests.get(self.zvmurl + self.endPoint + '/entities', headers=self.headerwithkey, verify=False)
        print(response)
        return response

    def validAlertHelpIdentifiersValues(self):

        response = requests.get(self.zvmurl + self.endPoint + '/helpidentifiers', headers=self.headerwithkey, verify=False)
        print(response)
        return response

    def validAlertLevelValues(self):

        response = requests.get(self.zvmurl + self.endPoint + '/levels', headers=self.headerwithkey, verify=False)
        print(response)
        return response

    def dismissAlert(self, alertid):

        response = requests.post(self.zvmurl + self.endPoint + '/levels' + str(alertid) + '/dismiss', headers=self.headerwithkey, verify=False)
        print(response)
        return response

    def undismissAlert(self, alertid):

        response = requests.post(self.zvmurl + self.endPoint + '/levels' + str(alertid) + '/undismiss', headers=self.headerwithkey, verify=False)
        print(response)
        return response

class datastores():
    endPoint = '/datastores'

    def __init__(self, zvmurl, headerwithkey, datastoreid=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.datastoreid = datastoreid

    def datastoreInfo(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def datastoreSingleInfo(self, datastoreid):
        response = requests.get(self.zvmurl + self.endPoint + '/' + str(datastoreid), headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

class events():
    endPoint = '/events'

    def __init__(self, zvmurl, headerwithkey, eventid=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.datastoreid = eventid

    def allEvents(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    #def filteredEvents(self):

        # TODO: Create filteredEvents function

    def getSingleEvent(self, eventid):
        response = requests.get(self.zvmurl + self.endPoint + '/' + str(eventid), headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidEventCategories(self):
        response = requests.get(self.zvmurl + self.endPoint + '/categories', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidEventEntities(self):
        response = requests.get(self.zvmurl + self.endPoint + '/entities', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidEventTypes(self):
        response = requests.get(self.zvmurl + self.endPoint + '/types', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


class license():
    endPoint = '/license'

    def __init__(self, zvmurl, headerwithkey, licensekey=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.licensekey = licensekey

    def addLicense(self):

        response = requests.put(self.zvmurl + self.endPoint, data=json.dumps({"LicenseKey": self.licensekey}), headers=self.headerwithkey, verify=False)
        print(response)

    def delLicense(self):

        response = requests.delete(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response)

    def getLicense(self):

        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

class localsite():
    endPoint = '/localsite'

    def __init__(self, zvmurl, headerwithkey):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey

    def getLocalSiteInfo(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidPairingStatus(self):
        response = requests.get(self.zvmurl + self.endPoint + '/pairingstatuses', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def sendBillingData(self):
        response = requests.post(self.zvmurl + self.endPoint + '/billing/sendUsage', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


'''
class volumes():
    endPoint = '/volumes'

    def __init__(self, ):

        def getAllVolumeInfo(headerwithkey, zvm_url):


        response = requests.get(zvm_url + endPoint, headers=headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response
'''