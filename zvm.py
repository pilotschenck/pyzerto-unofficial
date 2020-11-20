import json
import requests

class zvm:

    def __init__(self, zvmurl, headerwithkey):
        self.zvmurl = 'https://' + zvmurl + ':9669/v1'
        self.headerwithkey = headerwithkey

    def infoAllAlerts(self, alertid=None):

        return requests.get(self.zvmurl + '/alerts', headers=self.headerwithkey, verify=False)

    def infoSingleAlert(self, alertid):

        return requests.get(self.zvmurl + '/alerts/' + str(alertid), headers=self.headerwithkey, verify=False)

    def validAlertEntitiesValues(self):

        return requests.get(self.zvmurl + '/alerts/entities', headers=self.headerwithkey, verify=False)

    def validAlertHelpIdentifiersValues(self):

        return requests.get(self.zvmurl + '/alerts/helpidentifiers', headers=self.headerwithkey, verify=False)

    def validAlertLevelValues(self):

        return requests.get(self.zvmurl + '/alerts/levels', headers=self.headerwithkey, verify=False)

    def dismissAlert(self, alertid):

        return requests.post(self.zvmurl + '/alerts/levels' + str(alertid) + '/dismiss', headers=self.headerwithkey, verify=False)

    def undismissAlert(self, alertid):

        return requests.post(self.zvmurl + '/alerts/levels' + str(alertid) + '/undismiss', headers=self.headerwithkey, verify=False)

    def datastoreInfo(self):

        return requests.get(self.zvmurl + '/datastores', headers=self.headerwithkey, verify=False)

    def datastoreSingleInfo(self, datastoreid):

        return requests.get(self.zvmurl + '/datastores/' + str(datastoreid), headers=self.headerwithkey, verify=False)

    def allEvents(self):
        return requests.get(self.zvmurl + '/events', headers=self.headerwithkey, verify=False)


    #def filteredEvents(self):

        # TODO: Create filteredEvents function

    def getSingleEvent(self, eventid):

        return requests.get(self.zvmurl + '/events/' + str(eventid), headers=self.headerwithkey, verify=False)

    def getValidEventCategories(self):

        return requests.get(self.zvmurl + '/events/categories', headers=self.headerwithkey, verify=False)

    def getValidEventEntities(self):

        return requests.get(self.zvmurl + '/events/entities', headers=self.headerwithkey, verify=False)

    def getValidEventTypes(self):

        return requests.get(self.zvmurl + '/events/types', headers=self.headerwithkey, verify=False)

    def addLicense(self, licensekey):

        return requests.put(self.zvmurl + '/license', data=json.dumps({"LicenseKey": licensekey}), headers=self.headerwithkey, verify=False)

    def delLicense(self):

        return requests.delete(self.zvmurl + '/license', headers=self.headerwithkey, verify=False)

    def getLicense(self):

        return requests.get(self.zvmurl + '/license', headers=self.headerwithkey, verify=False)

    def getLocalSiteInfo(self):

        return requests.get(self.zvmurl + '/localsite', headers=self.headerwithkey, verify=False)

    def getValidPairingStatus(self):

        return requests.get(self.zvmurl + '/localsite/pairingstatuses', headers=testHeaders, verify=False)

    def sendBillingData(self):

        return requests.post(self.zvmurl +'/localsite/billing/sendUsage', headers=testHeaders, verify=False)

    def getListOfPeerSites(self):

        return requests.get(self.zvmurl + '/peersites', headers=self.headerwithkey, verify=False)

    def getSinglePeerSites(self, siteidentifier):

        return requests.get(self.zvmurl + '/peersites/' + siteidentifier, headers=self.headerwithkey, verify=False)

    def getStatusOfPeerSites(self):

        return requests.get(self.zvmurl + '/peersites/pairingstatuses', headers=self.headerwithkey, verify=False)

    def generatePeeringToken(self):

        return requests.post(self.zvmurl + '/peersites/generatetoken', headers=self.headerwithkey, verify=False)

    def pairToSite(self):
        # TODO: Finish this module
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getRecoveryReport(self):

        return requests.get(self.zvmurl + '/reports/recovery', headers=self.headerwithkey, verify=False)

    def getResourcesReport(self):

        return requests.get(self.zvmurl + '/reports/resources', headers=self.headerwithkey, verify=False)

    def getAllTasks(self):

        return requests.get(self.zvmurl + '/tasks', headers=self.headerwithkey, verify=False)

    def getSingleTask(self, taskidentifier):

        return requests.get(self.zvmurl + '/tasks/' + taskidentifier, headers=self.headerwithkey, verify=False)

    def getValidTaskTypes(self):

        return requests.get(self.zvmurl + '/tasks/types', headers=self.headerwithkey, verify=False)

    def getAllVirtualizationSites(self):

        return requests.get(self.zvmurl + '/virtualizationsites', headers=self.headerwithkey, verify=False)

    def getSingleVirtualizationSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier, headers=self.headerwithkey, verify=False)

    def getStorageClustersAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/datastoreclusters', headers=self.headerwithkey, verify=False)

    def getStorageAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/datastores', headers=self.headerwithkey, verify=False)

    def getDevicesAtAllHosts(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/devices', headers=self.headerwithkey, verify=False)

    def getDevicesAtSingleHost(self, siteidentifier, hostidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/devices?hostIdentifier=' + hostidentifier, headers=self.headerwithkey, verify=False)

        # TODO: Verify this actually works, because the documentation contains what looks like a typo... -- Update -- It works. Doc bug...

    def getFoldersAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/folders', headers=self.headerwithkey, verify=False)

    def getHostClustersAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/hostclusters', headers=self.headerwithkey, verify=False)

    def getHostsAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/hosts', headers=self.headerwithkey, verify=False)

    def getSingleHostAtSite(self, siteidentifier, hostidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/hosts/' + hostidentifier, headers=self.headerwithkey, verify=False)

    def getNetworksAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/networks', headers=self.headerwithkey, verify=False)

    def getRepositoriesAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/repositories', headers=self.headerwithkey, verify=False)

    def getResourcePoolsAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/resourcepools', headers=self.headerwithkey, verify=False)

    def getUnprotectedVmsAtSite(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/vms', headers=self.headerwithkey, verify=False)

    def getVmInstanceTypes(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/vmInstanceTypes', headers=self.headerwithkey, verify=False)

    def getAvailablevNets(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/virtualNetworks', headers=self.headerwithkey, verify=False)

    def getAvailableSubnets(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/subnets', headers=self.headerwithkey, verify=False)

    def getSecurityGroups(self, siteidentifier):

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/securityGroups', headers=self.headerwithkey, verify=False)

    def getAllVolumes(self):

        return requests.get(self.zvmurl + '/volumes', headers=self.headerwithkey, verify=False)