import json 
import requests
#from zerto_auth import testUrl, testHeaders
class vra():
    """The VRAs API returns information about VRAs, allows installation of a single VRA or VRA group,
    uninstallation of a VRA, or editing of a VRA
    ...
    Attributes
    ----------
    zvmurl : str
        full path to the target Zerto Virtual Manager API endpoint, e.g. 'https://10.0.1.20:9669/v1'
    headerwithkey : dict
        python dict object with the required REST headers, including a valid session key.
    datastoreid : str
        optional attribute specifying a specific datastoreID for the VRA disks. Default is None.
    groupname: str
        optional attribute specifying a group for VRA to be associated to. Default is None. 
    hostid: str
        optional attribute specifying host for VRA to run on. Default is None. 
    hostrootpassword: str 
        optional attribute if VRA leverages ESXi Host Root Password for ZVM communication. Default is None. 
    ram: str
        optional attribute specifying VRA ram configuration (min 1 GB - max 16 GB). Default is None. 
    cpu: str
        optional attribute specifying VRA cpu configuration (min 1 - max 4). Default is None. 
    networkid: str
        optional attribute specifing VRA network ID. Default is None.
    publickey: str 
        optional attribute specifying use of VMware VIB. Default is None.
    gateway: str 
        optional attribute specifying default gateway. Default is None. 
    subnet: str
        optional attribute specifying network subnet. Default is None. 
    ipaddr: str 
        optional attribute specifying stating ip address. Default is None. 
    ipconfig: str 
        optional attribute specifying (Static / DHCP) IP configuration. Default is None.  
    Methods
    -------
    infoAllVRAs()
        Get info on all VRAs.
    upgradeGroupVRAs()
        Upgrade a group of VRAs which are specified in the vraid body
    upgradeVRA()
        Upgrade individual VRA
    installVRA()
        Install individual VRA
    editVRA()
        Edit individual VRA
    delVRA()
        Delete individual VRA
    """
    endPoint = '/vras'
    
    def __init__(self, zvmurl, headerwithkey):
       self.zvmurl = 'https://' + zvmurl + ':9669/v1'
       self.headerwithkey = headerwithkey 
       
    def infoAllVRAs(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response)
        return response
       
    def upgradeGroupVRAs(self):
        response = requests.post(self.zvmurl + self.endPoint + "/upgrade", headers=self.headerwithkey, data=self.vraid, verify=False)
        print(response)
        return response
    # TODO: Determine logic on how single VRA ID is passed vs multi VRA for upgrade  
    def upgradeVRA(self, vra_id):
        response = requests.post(self.zvmurl + self.endPoint +"/" + vra_id + "/upgrade", headers=self.headerwithkey, verify=False)
        print(response)
        return response

    def installVRA(self, vra_dict):
        response = requests.post(self.zvmurl + self.endPoint, headers=self.headerwithkey, data=vra_dict, verify=False)
        print(response)
        return response

    def editVRA(self, vra_dict):
        # TODO: convert this manual dict into something more scalable
        response = requests.put(self.zvmurl + self.endPoint +"/" + self.vraid, headers=self.headerwithkey, data=vra_json, verify=False)
        print(response)
    
    def delVRA(self, vraid):
        response = requests.delete(self.zvmurl + self.endPoint +"/" + vraid, headers=self.headerwithkey, verify=False)
        print(response)
        return response


