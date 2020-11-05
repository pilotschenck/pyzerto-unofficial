import json
import requests
import crudFunctions
from zerto_auth import testUrl, testHeaders

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

    def deleteVpg(self, vpgid):
        response = requests.delete(self.zvmurl + self.endPoint + '/' + vpgid, headers=self.headerwithkey, verify=False)
        print(response.text)
        print(response)
        return response