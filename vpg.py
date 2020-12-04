"""
The vpg.py module contains properly-formatted API calls for various Zerto VPG tasks, including 
gathering VPG info such as checkpoints, as well as performing actions such as fail over test, 
or fail over live. 
"""

import json
import requests
import crudFunctions

class vpgs():
    """
    the vpgs class houses VPG specific methods. 
    ...
    Attributes
    ----------
    zvmip: str
        the IP address of the target ZVM 
    
    headerwithkey : dict
        a properly formatted dict containing the following key:value pairs:
        {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            'x-zerto-session': str-type containing valid session key generated with zerto_auth.py
        }

    vpgid: str
        unique identifier for individual VPG

    body: dict

    Methods
    -------
    getInfoAllVpgs()
        Returns information for all VPGs
    
    getInfoSingleVPG(vpgid)
        Returns information for individual VPG
    
    getCheckpointsForVPG(vpgid)
        Returns all checkpoints for individual VPG

    getCheckpointStatsForVpg(vpgid)
        Returns earliest and latest checkpoint statistics for individual VPG

    getValidValuesForVpgEntities()
        Returns all valid values for VPG entity types

    getValidValuesForFailoverCommitPolicies()
        Returns all valid values for Failover commit polices

    getValidValuesForFailoverShutdownPolicies()
        Returns all valid values for Failover shutdown policies

    getValidValuesForVpgPriorities()
        Returns all valid values for VPG priorities

    getValidValuesForFailoverRetentionPolicies()
        Returns all valid values for Failover retention policies
    
    getValidValuesForVpgStatuses()
        Returns all valid values for VPG statuses

    getValidValuesForVpgSubstatuses()
        Returns all valid values for VPG substatuses
    
    generatePeeringToken()
        Generates site pairing token for pairing to ZVM / ZCA
    
    insertTaggedCheckpoint(vpgid, body)
        Inserts tagged checkpoint for individual VPG

    cloneVpg(vpgid, body)
        Performs Clone operation for individual VPG
    
    cloneAbort(vpgid, body)
        Aborts Clone operation for individual VPG

    failoverVpg(vpgid, body)
        Performs Failover operation for individual VPG

    commitFailover(vpgid, body)
        Performs commit of Failover operation for individual VPG
    
    rollbackFailover(vpgid, body)
        Performs rollback of Failover operation for individual VPG
    
    failoverTest(vpgid, body)
        Performs Failover Test operation for individual VPG

    stopFailoverTest(vpgid, body)
        Stops Failover Test operation for individual VPG

    forceSyncVpg(vpgid, body)
        Performs Force Sync operation for individual VPG

    moveVpg(pgid, body)
        Performs Move operation for individual VPG
    
    rollbackMoveVpg(vpgid, body)
        Rollback Move operation for individual VPG
    
    commitMove(vpgid, body)
        Performs a commit of Move operation for individual VPG

    pauseVpgProtection(vpgid, body)
        Pause VPG protection for individual VPG

    resumeVpgProtection(vpgid, body)
        Resume VPG protection for individual VPG

    deleteVpg(vpgid, body)
        Delete individual VPG 
    """
    endPoint = '/vpgs'

    def __init__(self, zvmip, headerwithkey, vpgid=None):
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
        vpgid: str
            unique identifier for individual VPG
        """

        self.zvmurl = 'https://' + zvmip + ':9669/v1'
        self.headerwithkey = headerwithkey
        self.vpgid = vpgid

    def getInfoAllVpgs(self):
        """
        Returns information on all VPGs
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)

    def getInfoSingleVpg(self, vpgid):
        """
        Returns information for individual VPG
        
        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want information returned on 

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)

    def getCheckpointsForVpg(self, vpgid):
        """
        Returns all checkpoints for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on 

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/checkpoints', headers=self.headerwithkey, verify=False)

    def getCheckpointStatsForVpg(self, vpgid):
        """
        Returns earliest and latest checkpoint statistics for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on 

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/checkpoints/stats', headers=self.headerwithkey, verify=False)

    def getValidValuesForVpgEntities(self):
        """
        Returns all valid values for VPG entity types
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/entitytypes', headers=self.headerwithkey, verify=False)
    
    def getValidValuesForFailoverCommitPolicies(self):
        """
        Returns all valid values for Failover commit polices
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/failovercommitpolicies', headers=self.headerwithkey, verify=False)
        
    def getValidValuesForFailoverShutdownPolicies(self):
        """
        Returns all valid values for Failover shutdown polices
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/failovershutdownpolicies', headers=self.headerwithkey, verify=False)
        
    def getValidValuesForVpgPriorities(self):
        """
        Returns all valid values for VPG priorities
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/priorities', headers=self.headerwithkey, verify=False)

    def getValidValuesForFailoverRetentionPolicies(self):
        """
        Returns all valid values for Failover Retention polices
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/retentionpolicies', headers=self.headerwithkey, verify=False)

    def getValidValuesForVpgStatuses(self):
        """
        Returns all valid values for VPG Statuses
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/statuses', headers=self.headerwithkey, verify=False)
        
    def getValidValuesForVpgSubstatuses(self):
        """
        Returns all valid values for VPG Substatuses
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmurl + self.endPoint + '/substatuses', headers=self.headerwithkey, verify=False)
        
    def generatePeeringToken(self):
        """
        Generates site pairing token for pairing to ZVM / ZCA
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/generatetoken', headers=self.headerwithkey, verify=False)
        
    def insertTaggedCheckpoint(self, vpgid, body):
        """
        Inserts tagged checkpoint for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
            A properly formatted dict containing the following key:value pairs:
                {  
                    "checkpointName": "String content"
                }
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/Checkpoints', body = body, headers=self.headerwithkey, verify=False)
        
    def cloneVpg(self, vpgid, body):
        """
        Performs Clone operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
            A properly formatted dict containing the following key:value pairs:
                {  
                    "CheckpointId": "String content",
                    "DatastoreIdentifier": "String content",
                    "VmIdentifiers":
                    [  
                        VmIdentifier": "string content"
                    ]
                }
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/CloneStart', body = body, headers=self.headerwithkey, verify=False)
        
    def cloneAbort(self, vpgid):
        """
        Aborts Clone operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on 

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/CloneAbort', headers=self.headerwithkey, verify=False)

    def failoverVpg(self, vpgid, body):
        """
        Performs Failover operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
            A properly formatted dict containing the following key:value pairs:
            {  
                "CheckpointIdentifier": "String content",
                "CommitPolicy":1,
                "ShutdownPolicy":0,
                "TimeToWaitBeforeShutdownInSec":2147483647,
                "IsReverseProtection": Boolean,
                "VmIdentifiers":
                [  
                    VmIdentifier": "string content"
                ]
            }

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/Failover', body = body, headers=self.headerwithkey, verify=False)
       
    def commitFailover(self, vpgid, body):
        """
        Commit Failover operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
        A properly formatted dict containing the following key:value pairs:
            {  
            "IsReverseProtection": Boolean
            }

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverCommit', body = body, headers=self.headerwithkey, verify=False)
        
    def rollbackFailover(self, vpgid):
        """
        Rollback Failover operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        Returns
        -------
        type requests.models.Response object
        """        
        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverRollback', headers=self.headerwithkey, verify=False)
       

    def failoverTest(self, vpgid, body):
        """
        Perform Failover Test operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
        A properly formatted dict containing the following key:value pairs:
            {  
                "CheckpointIdentifier": "String content",
                "VmIdentifiers":
                    [  
                        VmIdentifier": "string content"
                    ]
            }

        Returns
        -------
        type requests.models.Response object
        """
        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverTest', body = body, headers=self.headerwithkey, verify=False)

    def stopFailoverTest(self, vpgid, body):
        """
        Stop Failover Test operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
        A properly formatted dict containing the following key:value pairs:
            {  
                "FailoverTestSuccess": Boolean,
                "FailoverTestSummary": "String content"
            }

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverTestStop', body = body, headers=self.headerwithkey, verify=False)
        
    def forceSyncVpg(self, vpgid):
        """
        Perform Force Sync operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        Returns
        -------
        type requests.models.Response object
        """           
        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/forcesync', headers=self.headerwithkey, verify=False)

    def moveVpg(self, vpgid, body):
        """
        Perform Move operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
        A properly formatted dict containing the following key:value pairs:
        {  
            "CommitPolicy": "String content",
            "CommitPolicyTimeout": 2,
            "ForceShutdown": Boolean,
            "ReverseProtection": Boolean,
            "KeepSourceVms": Boolean,
            "ContinueOnPreScriptFailure": Boolean
        }

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/move', body = body, headers=self.headerwithkey, verify=False)

    def rollbackMoveVpg(self, vpgid):
        """
        Rollback Failover operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        Returns
        -------
        type requests.models.Response object
        """       

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/moveRollback', body = body, headers=self.headerwithkey, verify=False)

    def commitMove(self, vpgid, body):
        """
        Commit Move operation for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
        {  
            "ReverseProtection": Boolean,
            "KeepSourceVms": Boolean
        }

        Returns
        -------
        type requests.models.Response object
        """        
        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/moveCommit', body = body, headers=self.headerwithkey, verify=False)

    def pauseVpgProtection(self, vpgid):
        """
        Pause protection for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/pause', headers=self.headerwithkey, verify=False)

    def resumeVpgProtection(self, vpgid):
        """
        Resume protection for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/resume', headers=self.headerwithkey, verify=False)

    def deleteVpg(self, vpgid, body):
        """
        Delete VPG for individual VPG

        Parameters
        ----------
        vpgid : str, required
            The VPG identifier that you want checkpoint information returned on

        body: dict, required
        {  
            "Force": Boolean,
            "KeepRecoveryVolumes": Boolean
        }

        Returns
        -------
        type requests.models.Response object
        """           
        return requests.delete(self.zvmurl + self.endPoint + '/' + vpgid, data=body, headers=self.headerwithkey, verify=False)

class vpgSettings():
    endPoint = '/vpgSettings'

    def __init__(self, zvmurl, headerwithkey, vpgid=None, vmid=None, nicid=None, volumeid=None):
        self.zvmurl = 'https://' + zvmurl + ':9669/v1'
        self.headerwithkey = headerwithkey
        self.vpgid = vpgid
        self.vmid = vmid
        self.nicid = nicid
        self.volumeid = volumeid


    def getSettingsForVpgs(self):

        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getSettingsForSingleVpg(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getBasicVpgSettings(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/basic', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getBootVpgSettings(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/bootgroup', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getJournalVpgSettings(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/journal', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getLtrVpgSettings(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/ltr', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getNetworkVpgSettings(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/networks', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getVpgPriority(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/priority', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def getVpgRecoverySettings(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/recovery', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def getVpgScriptSettings(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/scripting', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def getAllVmSettingsForAVpg(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/vms', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def getVMSettingsForSingleVmInVpg(self, vpgid, vmid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getNICSettingsForSingleVmInVpg(self, vpgid, vmid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getNICSettingsForSingleVmInVpg(self, vpgid, vmid, nicid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics/' + nicid,
                                headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getVolumeSettingsForSingleVmInVpg(self, vpgid, vmid):
        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/volumes',
                                headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getSingleVolumeSettingsForSingleVmInVpg(self, vpgid, vmid, volumeid):
        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/volumes/' + volumeid,
                                headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def createNewVpgSettingsObject(self, argbody):

        response = requests.post(self.zvmurl + self.endPoint, data=argbody, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def createDefaultVpgLTRSettings(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/ltr', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def commitSettingsObject(self, vpgid):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/commit', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def addVmsToSettingObject(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/vms', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def editVpgSettingsObject(self, vpgid, argbody):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid, data=argbody, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def editBasicSettingsObject(self, vpgid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/basic', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def editBootSettingsObject(self, vpgid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/bootgroup', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def editJournalObject(self, vpgid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/journal', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def editLtrSettings(self, vpgid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/ltr', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def editNetworksObject(self, vpgid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/networks', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def editRecoveryObject(self, vpgid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/recovery', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def editScriptingObject(self, vpgid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/scripting', body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def editVmSettingsObject(self, vpgid, vmid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid, body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def editNicSettingsObject(self, vpgid, vmid, nicid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics' + nicid, body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def editVolumeSettingsObject(self, vpgid, vmid, volumeid, body):
        response = requests.put(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/volumes/' + volumeid, body=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteSettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteBasicSettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/basic', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteBootSettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/bootgroup', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteJournalSettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/journal', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteLTRSettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/ltr', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteNetworkSettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/networks', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteRecoverySettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/recovery', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteScriptSettingsObject(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/scripting', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteVMSettingsFromAVpg(self, vpgid, vmid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteNicSettingsObject(self, vpgid, vmid, nicid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics/' + nicid, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response
