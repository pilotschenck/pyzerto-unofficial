import json
import requests
import crudFunctions
from zerto_auth import testUrl, testHeaders

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

    #def __init__(self, zvmurl, headerwithkey, licensekey=None):
    #    self.zvmurl = testUrl
    #    self.headerwithkey = testHeaders
    #    self.licensekey = licensekey

    def addLicense(self):

        response = requests.put(self.zvmurl + self.endPoint, data=json.dumps({"LicenseKey": self.licensekey}), headers=self.headerwithkey, verify=False)
        print(response)

    def delLicense(self, headers=None):

        response = requests.delete(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response)

    def getLicense():

        response = requests.get(testUrl+license.endPoint, headers=testHeaders, verify=False)
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

class peersites():
    endPoint = '/peersites'

    def __init__(self, zvmurl, headerwithkey, siteidentifier=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.siteidentifier = siteidentifier

    def getListOfPeerSites(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getSinglePeerSites(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getStatusOfPeerSites(self):
        response = requests.get(self.zvmurl + self.endPoint + '/pairingstatuses', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def generatePeeringToken(self):
        response = requests.post(self.zvmurl + self.endPoint + '/generatetoken', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def pairToSite(self):
        # TODO: Finish this module
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

class reports():
    endPoint = '/reports'

    def __init__(self, zvmurl, headerwithkey):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey

    def getRecoveryReport(self):
        response = requests.get(self.zvmurl + self.endPoint + '/recovery', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getResourcesReport(self):
        response = requests.get(self.zvmurl + self.endPoint + '/resources', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

class tasks():
    endPoint = '/tasks'

    def __init__(self, zvmurl, headerwithkey, taskidentifier=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.taskidentifier = taskidentifier

    def getAllTasks(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getSingleTask(self, taskidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + taskidentifier, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidTaskTypes(self):
        response = requests.get(self.zvmurl + self.endPoint + '/types', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

class virtualizationsites():
    endPoint = '/virtualizationsites'

    def __init__(self, zvmurl, headerwithkey, siteidentifier=None, hostidentifier=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.siteidentifier = siteidentifier
        self.hostidentifier = hostidentifier

    def getAllVirtualizationSites(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getSingleVirtualizationSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getStorageClustersAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/datastoreclusters', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getStorageAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/datastores', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getDevicesAtAllHosts(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/devices', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getDevicesAtSingleHost(self, siteidentifier, hostidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/devices?hostIdentifier=' + hostidentifier, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response
        # TODO: Verify this actually works, because the documentation contains what looks like a typo...

    def getFoldersAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/folders', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getHostClustersAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/hostclusters', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getHostsAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/hosts', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getSingleHostAtSite(self, siteidentifier, hostidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/hosts/' + hostidentifier, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getNetworksAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/networks', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getRepositoriesAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/repositories', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getResourcePoolsAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/resourcepools', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getUnprotectedVmsAtSite(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/vms', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getVmInstanceTypes(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/publicCloud/vmInstanceTypes', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getAvailablevNets(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/publicCloud/virtualNetworks', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getAvailableSubnets(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/publicCloud/subnets', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getSecurityGroups(self, siteidentifier):
        response = requests.get(self.zvmurl + self.endPoint + '/' + siteidentifier + '/publicCloud/securityGroups', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

class volumes():
    endPoint = '/volumes'

    def __init__(self, zvmurl, headerwithkey):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey

    def getAllVolumes(self):

        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response