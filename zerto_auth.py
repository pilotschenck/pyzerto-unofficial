import requests, urllib3
from requests.auth import HTTPBasicAuth
import json
import zvm, vpg, vra
from secrets import zvm_ip, zvm_u, zvm_p, zca_u, zerto_license, zerto_tag
import vmware.vapi.vsphere.client
import time


def login(zvm_ip, zvm_user, zvm_password):
    sessionUrl = 'https://' + zvm_ip + ':9669/v1/session/add'
    print("Getting API token for " + zvm_ip + "...")
    auth_info = "{\r\n\t\"AuthenticationMethod\":1\r\n}"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        }

    response = requests.post(sessionUrl, headers=headers, data=auth_info, verify=False, auth=HTTPBasicAuth(zvm_user,
                                                                                                          zvm_password))
    if response.ok:
        auth_token = response.headers['x-zerto-session']
        print("Api Token: " + auth_token)
        headers['x-zerto-session'] = auth_token
        print(headers)
        return headers

    else:
        print("HTTP %i - %s, Message %s" % (response.status_code, response.reason, response.text))


def constructTagProtectedVpg(tagname):

    protectedTag = tagname
    vmlist = vsphere_client.vcenter.VM.list()
    taglist = vsphere_client.tagging.Tag.list()
    friendlyTagList = []
    curatedTagList = []

    for i in range(len(taglist)):
        friendlyTagList.append(vsphere_client.tagging.Tag.get(taglist[i]))

    for i in range(len(friendlyTagList)):
        if friendlyTagList[i].name == protectedTag:
            curatedTagList.append(friendlyTagList[i].id)

    toBeProtectedVMs = vsphere_client.tagging.TagAssociation.list_attached_objects_on_tags(curatedTagList)

    for i in range(len(toBeProtectedVMs[0].object_ids)):
        print(toBeProtectedVMs[0].object_ids[i].id)
        workingDict = {"VmIdentifier": str(vCenterUUID+'.' + toBeProtectedVMs[0].object_ids[i].id)}
        workingOpen['Vms'].append(workingDict)

    payload2 = json.dumps(workingOpen)
    return payload2
    #return v.createNewVpgSettingsObject(payload2).json()


terraformWf = open('terraformvariables.json')  # Grab ZCA specific information from 'terraform output -json'
terraformVars = json.load(terraformWf)
terraformWf.close()
ipOfZca = terraformVars.get('SecondZCAprivateIPaddress').get('value')
pwOfZca = terraformVars.get('ZCADecrypted_Password').get('value')

'''

wf = open('testVpg.json')
payload = json.dumps(json.load(wf))
'''

wf2 = open('automatedVpgSkel.json')
workingOpen = json.load(wf2)
wf2.close()


vCenterUUID = '0ad85e47-6b7d-4a95-a60d-be3d79308223'

session = requests.session()
session.verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
vsphere_client = vmware.vapi.vsphere.client.create_vsphere_client(server="192.168.1.41", username=zvm_u, password=zvm_p, session=session)

testVraDict = {
                "DatastoreIdentifier":"0ad85e47-6b7d-4a95-a60d-be3d79308223.datastore-10",
                "HostIdentifier":"0ad85e47-6b7d-4a95-a60d-be3d79308223.host-9",
                "HostRootPassword":zvm_p,
                "MemoryInGb":3,
                "NumOfCpus":1,
                "NetworkIdentifier":"0ad85e47-6b7d-4a95-a60d-be3d79308223.network-11",
                "UsePublicKeyInsteadOfCredentials":False,
                "PopulatePostInstallation":False,
                "VraNetworkDataApi":{
                    "DefaultGateway":"192.168.1.72",
                    "SubnetMask":"255.255.255.0",
                    "VraIPAddress":"192.168.1.80",
                    "VraIPConfigurationTypeApi":"Static"
                    }
                }

def multiPlatformDemo():

    vczvmSession = login(zvm_ip, zvm_u, zvm_p)
    awszcaSession = login(ipOfZca, zca_u, pwOfZca)
    z = zvm.zvm(zvm_ip, vczvmSession)
    z.addLicense(zerto_license)
    v = vpg.vpgSettings(zvm_ip, vczvmSession)
    zvmvra = vra.vra(zvm_ip, vczvmSession)
    zvmvra.installVRA(json.dumps(testVraDict))
    zca = zvm.zvm(ipOfZca, awszcaSession)
    zca.addLicense(zerto_license)
    zcaTokenObject = zca.generatePeeringToken()
    zcaTokenActual = zcaTokenObject.json().get('Token')
    testOutput = requests.post('https://' + zvm_ip +':9669/v1/peersites', headers=vczvmSession, data=json.dumps(
                                {"HostName": ipOfZca, "Port":"9071", "Token":zcaTokenActual}), verify=False)
    time.sleep(100)

    workingOpen['Basic']['ProtectedSiteIdentifier'] = z.getLocalSiteInfo().json()['SiteIdentifier']
    workingOpen['Basic']['RecoverySiteIdentifier'] = z.getLocalSiteInfo().json()['SiteIdentifier']
    tagYoureIt=v.createNewVpgSettingsObject(constructTagProtectedVpg(zerto_tag)).json()
    #tagYoureIt=json.loads(constructTagProtectedVpg(zerto_tag))
    v.commitSettingsObject(tagYoureIt)




# v = vpg.vpgSettings(testUrl, testHeaders)
# newVpg = v.createNewVpgSettingsObject(payload)
# v.commitSettingsObject(newVpg)

# TODO: Return entire header as opposed to just key

# TODO: Securely pass credentials without storing in memory

# TODO: Error handle 401, 403, etc.

