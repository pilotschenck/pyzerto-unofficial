"""
The zvm.py module contains properly-formatted API calls for various Zerto Virtual Manager (or ZCA Zerto Virtual Manager
 service) tasks, including alert management, site pairing, site information gathering, and license management.
"""

import json
import requests


class zvm:
    """
    The zvm class houses ZVM-specific methods.

    ...

    Attributes
    ----------
    zvmip : str
        the IP address of the target ZVM

    headerwithkey : dict
        a properly formatted dict containing the following key:value pairs:
        {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            'x-zerto-session': str-type containing valid session key generated with zerto_auth.py
        }

    Methods
    -------
    infoAllAlerts(alertid=None)
        Returns information on all alerts

    infoSingleAlert(alertid)
        Returns information on a single alert

    validAlertEntitiesValues()
        Returns information on valid alert entities

    validAlertHelpIdentifiersValues()
        Returns information on valid alert help identifiers

    validAlertLevelValues()
        Returns information on valid alert levels

    dismissAlert(alertid)
        Dismisses an active alert

    undismissAlert(alertid)
        "Undismisses" (makes active) a previously-acknowledged/dismissed alert

    datastoreInfo()
        Returns information on locally available datastores for use as a replication target.

    datastoreSingleInfo(datastoreid)
        Returns information on a specific datastore locally available for use as a replication target.

    allEvents()
        Returns information on all (recent) events stored by the ZVM.

    filteredEvents()
        UNDER CONSTRUCTION. Function not yet usable.

    getSingleEvent(eventid)
        Returns information on a single event currently stored by the ZVM.

    getValidEventCategories()
        Returns all valid event categories.

    getValidEventEntities()
        Returns valid event entities.

    getValidEventTypes()
        Returns valid event types.

    addLicense(licensekey)
        Accepts a str parameter containing a valid Zerto license key and applies it to the target ZVM or ZCA.

    delLicense()
        Removes the license currently applied to the target ZVM or ZCA.

    getLicense()
        Returns information on the license applied to the target ZVM or ZCA.

    getLocalSiteInfo()
        Returns local site information.

    getValidPairingStatus()
        Returns information on the pairing status of the target ZVM or ZCA to other sites (ie other ZVMs or ZCAs).

    sendBillingData()
        Sends billing data to Zerto Analytics. Meant for use by Zerto Cloud Provider partners.

    getListOfPeerSites()
        Returns information about all peer sites of the target ZVM/ZCA.

    getSinglePeerSites(siteidentifier)
        Returns information about a specific peer site of the target ZVM/ZCA.

    getStatusOfPeerSites()
        Returns information on the status of all peer sites of the target ZVM/ZCA.

    generatePeeringToken()
        Returns a peering token that can then be passed to a desired peer site for the sake of the peering handshake.

    pairToSite()
        UNDER CONSTRUCTION. Function not yet usable.

    getRecoveryReport()
        Returns a recovery report for the target ZVM/ZCA.

    getResourcesReport()
        Returns a resources report for the target ZVM/ZCA.

    getAllTasks()
        Returns all tasks for the recovery ZVM/ZCA.

    getSingleTask(taskidentifier)
        Returns information on a single specified task for the ZVM/ZCA.

    getValidTaskTypes()
        Returns information on valid task types.

    getAllVirtualizationSites()
        Returns information on all virtualization sites.

    getSingleVirtualizationSite(siteidentifier)
        Returns information on a single specified virtualization site.

    getStorageClustersAtSite(siteidentifier)
        Returns information about storage clusters at a specific site available to the ZVM.

    getStorageAtSite(siteidentifier)
        Returns information about all storage at the specified site available to the ZVM/ZCA.

    getDevicesAtAllHosts(siteidentifier)
        Returns information about all devices at all hosts at the specified site to the ZVM/ZCA.

    getDevicesAtSingleHost(siteidentifier, hostidentifier)
        Returns information about all devices at a single host at the specified site to the ZVM/ZCA.

    getFoldersAtSite(siteidentifier)
        Returns information about all folders at the specified site.

    getHostClustersAtSite(siteidentifier)
        Returns information about all host clusters at the specified site.

    getHostsAtSite(siteidentifier)
        Returns information about all hosts at the specified site.

    getSingleHostAtSite(siteidentifier, hostidentifier)
        Returns information about a single host at the specified site.

    getNetworksAtSite(siteidentifier)
        Returns information about all networks at the specified site.

    getRepositoriesAtSite(siteidentifier)
        Returns information about all LTR repositories at the specified site.

    getResourcePoolsAtSite(siteidentifier)
        Returns information about all resource pools at the specified site.

    getUnprotectedVmsAtSite(siteidentifier)
        Returns information about unprotected VMs at the specified site.

    getVmInstanceTypes(siteidentifier)
        Returns information about instance types at the specified site.

    getAvailablevNets(siteidentifier)
        Returns information about available Azure vNets at the specified site.

    getAvailableSubnets(siteidentifier)
        Returns information about available Azure subnets at the specified site.

    getSecurityGroups(siteidentifier)
        Returns information about available security groups at the specified site.

    getAllVolumes()
        Returns information about available volumes visible to the ZVM/ZCA.
    """

    def __init__(self, zvmip, headerwithkey):
        """
        Parameters
        ----------
        zvmip : str
            The IP of the ZVM or ZCA
        headerwithkey : dict
            A properly formatted dict containing the following key:value pairs:
                {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                    'x-zerto-session': str-type containing valid session key generated with zerto_auth.py
                }
        """

        self.zvmurl = 'https://' + zvmip + ':9669/v1'
        self.headerwithkey = headerwithkey

    def infoAllAlerts(self):
        """
        Returns information on all alerts

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/alerts', headers=self.headerwithkey, verify=False)

    def infoSingleAlert(self, alertid):
        """
        Returns information on a single alert

        Parameters
        ----------
        alertid : str, required
            The alert identifier that you want information returned on

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/alerts/' + str(alertid), headers=self.headerwithkey, verify=False)

    def validAlertEntitiesValues(self):
        """
        Returns information on valid alert entities

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/alerts/entities', headers=self.headerwithkey, verify=False)

    def validAlertHelpIdentifiersValues(self):
        """
        Returns information on valid alert help identifiers

        Returns
        -------
        type requests.models.Response object

        """

        return requests.get(self.zvmurl + '/alerts/helpidentifiers', headers=self.headerwithkey, verify=False)

    def validAlertLevelValues(self):
        """
        Returns information on valid alert levels

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/alerts/levels', headers=self.headerwithkey, verify=False)

    def dismissAlert(self, alertid):
        """
        Dismisses an active alert

        Parameters
        ----------
        alertid : str, required
            The specific alert that you want to dismiss

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + '/alerts/levels' + str(alertid) + '/dismiss', headers=self.headerwithkey,
                             verify=False)

    def undismissAlert(self, alertid):
        """
        "Undismisses" (makes active) a previously-acknowledged/dismissed alert

        Parameters
        ----------
        alertid : str, required
            The specific alert that you want to undismiss

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + '/alerts/levels' + str(alertid) + '/undismiss', headers=self.headerwithkey,
                             verify=False)

    def datastoreInfo(self):
        """
        Returns information on locally available datastores for use as a replication target.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/datastores', headers=self.headerwithkey, verify=False)

    def datastoreSingleInfo(self, datastoreid):
        """
        Returns information on a specific datastore locally available for use as a replication target.

        Parameters
        ----------
        datastoreid : str, required
            The specific datastore that you want information on.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/datastores/' + str(datastoreid), headers=self.headerwithkey, verify=False)

    def allEvents(self):
        """
        Returns information on all (recent) events stored by the ZVM.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/events', headers=self.headerwithkey, verify=False)

    # def filteredEvents(self):

        # TODO: Create filteredEvents function

    def getSingleEvent(self, eventid):
        """
        Returns information on a single event currently stored by the ZVM.

        Parameters
        ----------
        eventid : str, required

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/events/' + str(eventid), headers=self.headerwithkey, verify=False)

    def getValidEventCategories(self):
        """
        Returns all valid event categories.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/events/categories', headers=self.headerwithkey, verify=False)

    def getValidEventEntities(self):
        """
        Returns valid event entities.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/events/entities', headers=self.headerwithkey, verify=False)

    def getValidEventTypes(self):
        """
        Returns valid event types.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/events/types', headers=self.headerwithkey, verify=False)

    def addLicense(self, licensekey):
        """
        Accepts a str parameter containing a valid Zerto license key and applies it to the target ZVM or ZCA.

        Parameters
        ----------
        licensekey : str
            The license key you want to apply to the ZVM/ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmurl + '/license', data=json.dumps({"LicenseKey": licensekey}),
                            headers=self.headerwithkey, verify=False)

    def delLicense(self):
        """
        Removes the license currently applied to the target ZVM or ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmurl + '/license', headers=self.headerwithkey, verify=False)

    def getLicense(self):
        """
        Returns information on the license applied to the target ZVM or ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/license', headers=self.headerwithkey, verify=False)

    def getLocalSiteInfo(self):
        """
        Returns local site information.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/localsite', headers=self.headerwithkey, verify=False)

    def getValidPairingStatus(self):
        """
        Returns information on the pairing status of the target ZVM or ZCA to other sites (ie other ZVMs or ZCAs).

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/localsite/pairingstatuses', headers=self.headerwithkey, verify=False)

    def sendBillingData(self):
        """
        Sends billing data to Zerto Analytics. Meant for use by Zerto Cloud Provider partners.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + '/localsite/billing/sendUsage', headers=self.headerwithkey, verify=False)

    def getListOfPeerSites(self):
        """
        Returns information about all peer sites of the target ZVM/ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/peersites', headers=self.headerwithkey, verify=False)

    def getSinglePeerSites(self, siteidentifier):
        """
        Returns information about a specific peer site of the target ZVM/ZCA.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID that you are wanting to get information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/peersites/' + siteidentifier, headers=self.headerwithkey, verify=False)

    def getStatusOfPeerSites(self):
        """
        Returns information on the status of all peer sites of the target ZVM/ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/peersites/pairingstatuses', headers=self.headerwithkey, verify=False)

    def generatePeeringToken(self):
        """
        Returns a peering token that can then be passed to a desired peer site for the sake of the peering handshake.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + '/peersites/generatetoken', headers=self.headerwithkey, verify=False)

    def pairToSite(self, peerip, pairingtoken):
        """
        Executes a pairing operation between the target ZVM/ZCA and a requested peer site.

        Parameters
        ----------
        peerip : str, required
            The IP address of the peer site you want to connect to.
        pairingtoken: str, required
            A valid pairing token generated by the desired peer site

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + '/peersites', headers=self.headerwithkey, data=json.dumps(
            {"HostName": peerip, "Port": "9071", "Token": pairingtoken}), verify=False)

    def getRecoveryReport(self):
        """
        Returns a recovery report for the target ZVM/ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/reports/recovery', headers=self.headerwithkey, verify=False)

    def getResourcesReport(self):
        """
        Returns a resources report for the target ZVM/ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/reports/resources', headers=self.headerwithkey, verify=False)

    def getAllTasks(self):
        """
        Returns all tasks for the recovery ZVM/ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/tasks', headers=self.headerwithkey, verify=False)

    def getSingleTask(self, taskidentifier):
        """
        Returns information on a single specified task for the ZVM/ZCA.

        Parameters
        ----------
        taskidentifier : str, required
            The task ID that you want information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/tasks/' + taskidentifier, headers=self.headerwithkey, verify=False)

    def getValidTaskTypes(self):
        """
        Returns information on valid task types.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/tasks/types', headers=self.headerwithkey, verify=False)

    def getAllVirtualizationSites(self):
        """
        Returns information on all virtualization sites.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites', headers=self.headerwithkey, verify=False)

    def getSingleVirtualizationSite(self, siteidentifier):
        """
        Returns information on a single specified virtualization site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want info about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier, headers=self.headerwithkey,
                            verify=False)

    def getStorageClustersAtSite(self, siteidentifier):
        """
        Returns information about storage clusters at a specific site available to the ZVM.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want storage cluster information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/datastoreclusters',
                            headers=self.headerwithkey, verify=False)

    def getStorageAtSite(self, siteidentifier):
        """
        Returns information about all storage at the specified site available to the ZVM/ZCA.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want storage information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/datastores',
                            headers=self.headerwithkey, verify=False)

    def getDevicesAtAllHosts(self, siteidentifier):
        """
        Returns information about all devices at all hosts at the specified site to the ZVM/ZCA.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want device information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/devices',
                            headers=self.headerwithkey, verify=False)

    def getDevicesAtSingleHost(self, siteidentifier, hostidentifier):
        """
        Returns information about all devices at a single host at the specified site to the ZVM/ZCA.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want device information about.

        hostidentifier : str, required
            The host ID of the specific host you want device information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/devices?hostIdentifier=' +
                            hostidentifier, headers=self.headerwithkey, verify=False)

        # TODO: Verify this actually works, because the documentation contains what looks like a typo...
        #  -- Update -- It works. Doc bug...

    def getFoldersAtSite(self, siteidentifier):
        """
        Returns information about all folders at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want folder information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/folders',
                            headers=self.headerwithkey, verify=False)

    def getHostClustersAtSite(self, siteidentifier):
        """
        Returns information about all host clusters at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
           The site ID of the site you want host cluster info about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/hostclusters',
                            headers=self.headerwithkey, verify=False)

    def getHostsAtSite(self, siteidentifier):
        """
        Returns information about all hosts at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want host information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/hosts',
                            headers=self.headerwithkey, verify=False)

    def getSingleHostAtSite(self, siteidentifier, hostidentifier):
        """
        Returns information about a single host at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want host information about.

        hostidentifier : str, required
            The host ID that you want information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/hosts/' + hostidentifier,
                            headers=self.headerwithkey, verify=False)

    def getNetworksAtSite(self, siteidentifier):
        """
        Returns information about all networks at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want network information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/networks',
                            headers=self.headerwithkey, verify=False)

    def getRepositoriesAtSite(self, siteidentifier):
        """
        Returns information about all LTR repositories at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want LTR repo information about

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/repositories',
                            headers=self.headerwithkey, verify=False)

    def getResourcePoolsAtSite(self, siteidentifier):
        """
        Returns information about all resource pools at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want resource pool information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/resourcepools',
                            headers=self.headerwithkey, verify=False)

    def getUnprotectedVmsAtSite(self, siteidentifier):
        """
        Returns information about unprotected VMs at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want unprotected VM information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/vms', headers=self.headerwithkey,
                            verify=False)

    def getVmInstanceTypes(self, siteidentifier):
        """
        Returns information about instance types at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want VM instance type information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/vmInstanceTypes',
                            headers=self.headerwithkey, verify=False)

    def getAvailablevNets(self, siteidentifier):
        """
        Returns information about available Azure vNets at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want vNet information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/virtualNetworks',
                            headers=self.headerwithkey, verify=False)

    def getAvailableSubnets(self, siteidentifier):
        """
        Returns information about available Azure subnets at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want subnet information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/subnets',
                            headers=self.headerwithkey, verify=False)

    def getSecurityGroups(self, siteidentifier):
        """
        Returns information about available security groups at the specified site.

        Parameters
        ----------
        siteidentifier : str, required
            The site ID of the site you want security group information about.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/virtualizationsites/' + siteidentifier + '/publicCloud/securityGroups',
                            headers=self.headerwithkey, verify=False)

    def getAllVolumes(self):
        """
        Returns information about available volumes visible to the ZVM/ZCA.

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + '/volumes', headers=self.headerwithkey, verify=False)
