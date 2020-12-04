"""
The vpg.py module contains properly-formatted API calls for various Zerto VPG tasks, including 
gathering VPG info such as checkpoints, as well as performing actions such as fail over test, 
or fail over live. 
"""

import requests

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

        self.zvmip = 'https://' + zvmip + ':9669/v1'
        self.headerwithkey = headerwithkey
        self.vpgid = vpgid

    def getInfoAllVpgs(self):
        """
        Returns information on all VPGs
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint, headers=self.headerwithkey, verify=False)

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

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)

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

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/checkpoints', headers=self.headerwithkey, verify=False)

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

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/checkpoints/stats', headers=self.headerwithkey, verify=False)

    def getValidValuesForVpgEntities(self):
        """
        Returns all valid values for VPG entity types
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/entitytypes', headers=self.headerwithkey, verify=False)
    
    def getValidValuesForFailoverCommitPolicies(self):
        """
        Returns all valid values for Failover commit polices
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/failovercommitpolicies', headers=self.headerwithkey, verify=False)
        
    def getValidValuesForFailoverShutdownPolicies(self):
        """
        Returns all valid values for Failover shutdown polices
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/failovershutdownpolicies', headers=self.headerwithkey, verify=False)
        
    def getValidValuesForVpgPriorities(self):
        """
        Returns all valid values for VPG priorities
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/priorities', headers=self.headerwithkey, verify=False)

    def getValidValuesForFailoverRetentionPolicies(self):
        """
        Returns all valid values for Failover Retention polices
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/retentionpolicies', headers=self.headerwithkey, verify=False)

    def getValidValuesForVpgStatuses(self):
        """
        Returns all valid values for VPG Statuses
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/statuses', headers=self.headerwithkey, verify=False)
        
    def getValidValuesForVpgSubstatuses(self):
        """
        Returns all valid values for VPG Substatuses
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/substatuses', headers=self.headerwithkey, verify=False)
        
    def generatePeeringToken(self):
        """
        Generates site pairing token for pairing to ZVM / ZCA
        
        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmip + self.endPoint + '/generatetoken', headers=self.headerwithkey, verify=False)
        
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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/Checkpoints', body = body, headers=self.headerwithkey, verify=False)
        
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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/CloneStart', body = body, headers=self.headerwithkey, verify=False)
        
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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/CloneAbort', headers=self.headerwithkey, verify=False)

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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/Failover', body = body, headers=self.headerwithkey, verify=False)
       
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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/FailoverCommit', body = body, headers=self.headerwithkey, verify=False)
        
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
        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/FailoverRollback', headers=self.headerwithkey, verify=False)
       

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
        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/FailoverTest', body = body, headers=self.headerwithkey, verify=False)

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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/FailoverTestStop', body = body, headers=self.headerwithkey, verify=False)
        
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
        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/forcesync', headers=self.headerwithkey, verify=False)

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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/move', body = body, headers=self.headerwithkey, verify=False)

    def rollbackMoveVpg(self, vpgid, body):
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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/moveRollback', body = body, headers=self.headerwithkey, verify=False)

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
        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/moveCommit', body = body, headers=self.headerwithkey, verify=False)

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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/pause', headers=self.headerwithkey, verify=False)

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

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/resume', headers=self.headerwithkey, verify=False)

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
        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid, data=body, headers=self.headerwithkey, verify=False)

class vpgSettings():
    """
    the vpgSettings class houses VPG "object" specific methods. Unlike the vpg class, the methods in vpgSettings apply
    to a VPG as a whole as opposed to what is inside a VPG. Use vpgSettings to create and commit VPGs into existence,
    get settings, and the like.
    ...
    Attributes
    ----------
    zvmip : str
        the IP address of the target ZVM or ZCA

    headerwithkey : dict
        a properly formatted dict containing the following key:value pairs:
        {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            'x-zerto-session': str-type containing valid session key generated with zerto_auth.py
        }

    vpgid : str (default: None)
        identifier for a VPG

    nicid : str (default: None)
        identifier for a single NIC

    volumeid : str (default: None)
        identifier of a volume

    Methods
    -------
    getSettingsForVpgs()
        Returns settings information for all VPGs

    getSettingsForSingleVpg(vpgid)
        Returns settings information for a single specified VPG

    getBasicVpgSettings(vpgid)
        Returns basic (ie, no granular VM) settings for a single specific VPG.

    getBootVpgSettings(vpgid)
        Returns boot group settings for a single specified VPG

    getJournalVpgSettings(vpgid)
        Returns journal settings for a single specified VPG

    getLtrVpgSettings(vpgid)
        Returns LTR settings information for a single specified VPG

    getNetworkVpgSettings(vpgid)
        Returns network settings for a single specified VPG

    getVpgPriority(vpgid)
        Returns the priority level for a single specified VPG

    getVpgRecoverySettings(vpgid)
        Returns recovery settings for a single specified VPG

    getVpgScriptSettings(vpgid)
        Returns pre- and post-recovery scripting information for a single specified VPG

    getAllVmSettingsForAVpg(vpgid)
        Returns all VM-related settings for a single specified VPG

    getVMSettingsForSingleVmInVpg(vpgid, vmid)
        Returns all settings for a single specified VM in a single specified VPG

    getNICSettingsForSingleVmInVpg(vpgid, vmid)
        Returns NIC settings for a single specified VM in a single specified VPG

    getSingleNICSettingsForSingleVmInVpg(vpgid, vmid, nicid)
        Returns settings for a single specified NIC in a single specified VM in a single specified VPG.

    getVolumeSettingsForSingleVmInVpg(vpgid, vmid)
        Returns volume settings for a single specified VM in a single specified VPG

    getSingleVolumeSettingsForSingleVmInVpg(vpgid, vmid, volumeid)
        Returns information about a single specified volume about a single specified VM in a single specified VPG

    createNewVpgSettingsObject(argbody)
        Creates an empty VPG settings object. This object is the foundation of a new VPG.

    createDefaultVpgLTRSettings(body)
        Creates a default LTR settings VPG object.

    commitSettingsObject(vpgid)
        Commits (closes) and executes the actual creation of a VPG after settings have been applied to the vpgid.

    addVmsToSettingObject(vpgid, body)
        Adds VMs to an open VPG settings object.

    editVpgSettingsObject(vpgid, argbody)
        Edits an open VPG settings object with the contents of argbody.

    editBasicSettingsObject(vpgid, body)
        Edits an open BasicSettingsObject with the contents of argbody.

    editBootSettingsObject(vpgid, body)
        Edits the boot group of an open VPG.

    editJournalObject(vpgid, body)
        Edits the journal of an open VPG.

    editLtrSettings(vpgid, body)
        Edits the LTR settings of an open VPG.

    editNetworksObject(vpgid, body)
        Edits the network settings of an open VPG.

    editRecoveryObject(vpgid, body)
        Edits the recovery objects of an open VPG.

    editScriptingObject(vpgid, body)
        Edits the scripting objects of an open VPG.

    editVmSettingsObject(vpgid, vmid, body)
        Edits the VM settings object of an open VPG.

    editNicSettingsObject(vpgid, vmid, nicid, body)
        Edits the NIC settings object of an open VPG.

    editVolumeSettingsObject(vpgid, vmid, volumeid, body)
        Edits the volume settings object of an open VPG.

    deleteSettingsObject(vpgid)
        Deletes a VPG Settings object.

    deleteBasicSettingsObject(vpgid)
        Deletes a BasicSettings object.

    deleteBootSettingsObject(vpgid)
        Deletes a boot settings object.

    deleteJournalSettingsObject(vpgid)
        Deletes a journal settings object.

    deleteLTRSettingsObject(vpgid)
        Deletes an LTR Settings object.

    deleteNetworkSettingsObject(vpgid)
        Deletes a Network Settings object.

    deleteRecoverySettingsObject(vpgid)
        Deletes a recovery settings object.

    deleteScriptSettingsObject(vpgid)
        Deletes a script settings object.

    deleteVMSettingsFromAVpg(vpgid, vmid)
        Deletes a VMSettings object.

    deleteNicSettingsObject(vpgid, vmid, nicid)
        Deletes a NIC settings object.
    """

    endPoint = '/vpgSettings'

    def __init__(self, zvmip, headerwithkey, vpgid=None, vmid=None, nicid=None, volumeid=None):
        """
        Parameters
        ----------
        zvmip : str, required
            IP address of target ZVM or ZCA

        headerwithkey : dict, required
            A properly formatted dict containing the following key:value pairs:
                {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                    'x-zerto-session': str-type containing valid session key generated with zerto_auth.py
                }

        vpgid : str, optional
            ID of the VPG in question

        vmid : str, optional
            ID of the VM in question

        nicid : str, optional
            ID of the NIC in question

        volumeid : str, optional
            ID of the volume in question
        """
        self.zvmip = 'https://' + zvmip + ':9669/v1'
        self.headerwithkey = headerwithkey
        self.vpgid = vpgid
        self.vmid = vmid
        self.nicid = nicid
        self.volumeid = volumeid


    def getSettingsForVpgs(self):
        """
        Returns settings information for all VPGs

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint, headers=self.headerwithkey, verify=False)

    def getSettingsForSingleVpg(self, vpgid):
        """
        Returns settings information for a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)

    def getBasicVpgSettings(self, vpgid):
        """
        Returns basic (ie, no granular VM) settings for a single specific VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/basic', headers=self.headerwithkey,
                            verify=False)

    def getBootVpgSettings(self, vpgid):
        """
        Returns boot group settings for a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/bootgroup', headers=self.headerwithkey,
                            verify=False)

    def getJournalVpgSettings(self, vpgid):
        """
        Returns journal settings for a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/journal', headers=self.headerwithkey,
                            verify=False)

    def getLtrVpgSettings(self, vpgid):
        """
        Returns LTR settings information for a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/ltr', headers=self.headerwithkey, verify=False)

    def getNetworkVpgSettings(self, vpgid):
        """
        Returns network settings for a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/networks', headers=self.headerwithkey, verify=False)

    def getVpgPriority(self, vpgid):
        """
        Returns the priority level for a single specified VPG

        Parameters
        ----------
        vpgid: str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/priority', headers=self.headerwithkey, verify=False)

    def getVpgRecoverySettings(self, vpgid):
        """
        Returns recovery settings for a single specified VPG

        Parameters
        ----------
        vpgid: str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/recovery', headers=self.headerwithkey, verify=False)

    def getVpgScriptSettings(self, vpgid):
        """
        Returns pre- and post-recovery scripting information for a single specified VPG

        Parameters
        ----------
        vpgid: str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/scripting', headers=self.headerwithkey, verify=False)

    def getAllVmSettingsForAVpg(self, vpgid):
        """
        Returns all VM-related settings for a single specified VPG

        Parameters
        ----------
        vpgid: str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/vms', headers=self.headerwithkey, verify=False)

    def getVMSettingsForSingleVmInVpg(self, vpgid, vmid):
        """
        Returns all settings for a single specified VM in a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid, headers=self.headerwithkey, verify=False)

    def getNICSettingsForSingleVmInVpg(self, vpgid, vmid):
        """
        Returns NIC settings for a single specified VM in a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics', headers=self.headerwithkey, verify=False)

    def getSingleNICSettingsForSingleVmInVpg(self, vpgid, vmid, nicid):
        """
        Returns settings for a single specified NIC in a single specified VM in a single specified VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question
        nicid : str, required
            ID of the NIC in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics/' + nicid,
                                headers=self.headerwithkey, verify=False)

    def getVolumeSettingsForSingleVmInVpg(self, vpgid, vmid):
        """
        Returns volume settings for a single specified VM in a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/volumes',
                                headers=self.headerwithkey, verify=False)

    def getSingleVolumeSettingsForSingleVmInVpg(self, vpgid, vmid, volumeid):
        """
        Returns information about a single specified volume about a single specified VM in a single specified VPG

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question
        volumeid : str, required
            ID of the volume in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.get(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/volumes/' + volumeid,
                                headers=self.headerwithkey, verify=False)

    def createNewVpgSettingsObject(self, argbody):
        """
        Creates an empty VPG settings object. This object is the foundation of a new VPG.

        Parameters
        ----------
        argbody : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf
        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmip + self.endPoint, data=argbody, headers=self.headerwithkey, verify=False)

    def createDefaultVpgLTRSettings(self, vpgid, body):
        """
        Creates a default LTR settings VPG object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/ltr', body=body, headers=self.headerwithkey, verify=False)

    def commitSettingsObject(self, vpgid):
        """
        Commits (closes) and executes the actual creation of a VPG after settings have been applied to the vpgid.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/commit', headers=self.headerwithkey, verify=False)

    def addVmsToSettingObject(self, vpgid, body):
        """
        Adds VMs to an open VPG settings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.post(self.zvmip + self.endPoint + '/' + vpgid + '/vms', body=body, headers=self.headerwithkey, verify=False)

    def editVpgSettingsObject(self, vpgid, argbody):
        """
        Edits an open VPG settings object with the contents of argbody.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        argbody : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid, data=argbody, headers=self.headerwithkey, verify=False)

    def editBasicSettingsObject(self, vpgid, body):
        """
        Edits an open BasicSettingsObject with the contents of argbody.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/basic', body=body, headers=self.headerwithkey, verify=False)

    def editBootSettingsObject(self, vpgid, body):
        """
        Edits the boot group of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/bootgroup', body=body, headers=self.headerwithkey, verify=False)

    def editJournalObject(self, vpgid, body):
        """
        Edits the journal of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/journal', body=body, headers=self.headerwithkey, verify=False)

    def editLtrSettings(self, vpgid, body):
        """
        Edits the LTR settings of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/ltr', body=body, headers=self.headerwithkey, verify=False)

    def editNetworksObject(self, vpgid, body):
        """
        Edits the network settings of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/networks', body=body, headers=self.headerwithkey, verify=False)

    def editRecoveryObject(self, vpgid, body):
        """
        Edits the recovery objects of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/recovery', body=body, headers=self.headerwithkey, verify=False)

    def editScriptingObject(self, vpgid, body):
        """
        Edits the scripting objects of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/scripting', body=body, headers=self.headerwithkey, verify=False)

    def editVmSettingsObject(self, vpgid, vmid, body):
        """
        Edits the VM settings object of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid, body=body, headers=self.headerwithkey, verify=False)

    def editNicSettingsObject(self, vpgid, vmid, nicid, body):
        """
        Edits the NIC settings object of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question
        nicid : str, required
            ID of the NIC in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics' + nicid, body=body, headers=self.headerwithkey, verify=False)

    def editVolumeSettingsObject(self, vpgid, vmid, volumeid, body):
        """
        Edits the volume settings object of an open VPG.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question
        vmid : str, required
            ID of the VM in question
        volumeid : str, required
            ID of the volume in question
        body : dict, required
            Properly formatted JSON body. See Zerto API documentation:
            http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20RESTful%20APIs.pdf

        Returns
        -------
        type requests.models.Response object
        """

        return requests.put(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/volumes/' + volumeid, body=body, headers=self.headerwithkey, verify=False)

    def deleteSettingsObject(self, vpgid):
        """
        Deletes a VPG Settings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)

    def deleteBasicSettingsObject(self, vpgid):
        """
        Deletes a BasicSettings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/basic', headers=self.headerwithkey, verify=False)

    def deleteBootSettingsObject(self, vpgid):
        """
        Deletes a boot settings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/bootgroup', headers=self.headerwithkey, verify=False)

    def deleteJournalSettingsObject(self, vpgid):
        """
        Deletes a journal settings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/journal', headers=self.headerwithkey, verify=False)

    def deleteLTRSettingsObject(self, vpgid):
        """
        Deletes an LTR Settings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/ltr', headers=self.headerwithkey, verify=False)

    def deleteNetworkSettingsObject(self, vpgid):
        """
        Deletes a Network Settings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/networks', headers=self.headerwithkey, verify=False)

    def deleteRecoverySettingsObject(self, vpgid):
        """
        Deletes a recovery settings object.

        Parameters
        ----------
        vpgid : str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/recovery', headers=self.headerwithkey, verify=False)

    def deleteScriptSettingsObject(self, vpgid):
        """
        Deletes a script settings object.

        Parameters
        ----------
        vpgid: str, required
            ID of the VPG in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/scripting', headers=self.headerwithkey, verify=False)

    def deleteVMSettingsFromAVpg(self, vpgid, vmid):
        """
        Deletes a VMSettings object.

        Parameters
        ----------
        vpgid: str, required
            ID of the VPG in question
        vmid: str, required
            ID of the VM in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid, headers=self.headerwithkey, verify=False)

    def deleteNicSettingsObject(self, vpgid, vmid, nicid):
        """
        Deletes a NIC settings object.

        Parameters
        ----------
        vpgid: str, required
            ID of the VPG in question
        vmid: str, required
            ID of the VM in question
        nicid: str, required
            ID of the NIC in question

        Returns
        -------
        type requests.models.Response object
        """

        return requests.delete(self.zvmip + self.endPoint + '/' + vpgid + '/vms/' + vmid + '/nics/' + nicid, headers=self.headerwithkey, verify=False)
