import json
import requests
import crudFunctions


class vpgs():
    endPoint = '/vpgs'

    def __init__(self, zvmurl, headerwithkey, vpgid=None):
        self.zvmurl = zvmurl
        self.headerwithkey = headerwithkey
        self.vpgid = vpgid

    def getInfoAllVpgs(self):

        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getInfoSingleVpg(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getCheckpointsForVpg(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/checkpoints', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def getCheckpointStatsForVpg(self, vpgid):

        response = requests.get(self.zvmurl + self.endPoint + '/' + vpgid + '/checkpoints/stats', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def getValidValuesForVpgEntities(self):

        response = requests.get(self.zvmurl + self.endPoint + '/entitytypes', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response


    def getValidValuesForFailoverCommitPolicies(self):

        response = requests.get(self.zvmurl + self.endPoint + '/failovercommitpolicies', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidValuesForFailoverShutdownPolicies(self):

        response = requests.get(self.zvmurl + self.endPoint + '/failovershutdownpolicies', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidValuesForVpgPriorities(self):

        response = requests.get(self.zvmurl + self.endPoint + '/priorities', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidValuesForFailoverRetentionPolicies(self):

        response = requests.get(self.zvmurl + self.endPoint + '/retentionpolicies', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidValuesForVpgStatuses(self):

        response = requests.get(self.zvmurl + self.endPoint + '/statuses', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def getValidValuesForVpgSubstatuses(self):

        response = requests.get(self.zvmurl + self.endPoint + '/substatuses', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def generatePeeringToken(self):
        response = requests.post(self.zvmurl + self.endPoint + '/generatetoken', headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def insertTaggedCheckpoint(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/Checkpoints', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def cloneVpg(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/CloneStart', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def cloneAbort(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/CloneAbort', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def failoverVpg(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/Failover', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def commitFailover(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverCommit', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def rollbackFailover(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverRollback', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def failoverTest(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverTest', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def stopFailoverTest(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/FailoverTestStop', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def forceSyncVpg(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/forcesync', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def moveVpg(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/move', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def rollbackMoveVpg(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/moveRollback', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def commitMove(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/moveCommit', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def pauseVpgProtection(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/pause', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def resumeVpgProtection(self, vpgid, body):
        response = requests.post(self.zvmurl + self.endPoint + '/' + vpgid + '/resume', body = body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

    def deleteVpg(self, vpgid, body):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid, data=body, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response

class vpgSettings():
    endPoint = '/vpgSettings'

    def __init__(self, zvmurl, headerwithkey, vpgid=None, vmid=None, nicid=None, volumeid=None):
        self.zvmurl = zvmurl
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
