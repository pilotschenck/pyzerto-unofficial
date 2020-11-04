import json 
import requests


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
    """
    endPoint = '/vras'
    #This is a class for VRAs 
    def __init__(self, zvmurl, headerwithkey, datastoreid=None, groupname=None, hostid=None, hostrootpassword=None, 
       ram=None, cpu=None, networkid=None, publickey=None, gateway=None, subnet=None, ipaddr=None,ipconfig=None):
       self.zvmurl = zvmurl
       self.headerwithkey = headerwithkey
       self.datastoreid = datastoreid
       self.groupname = groupname
       self.host = hostid
       self.hostpass = hostrootpassword
       self.ram = ram
       self.cpu = cpu 
       self.networkid = networkid
       self.hostkey = publickey
       self.gateway = gateway 
       self.subnet = subnet
       self.ipaddr = ipaddr
       self.ipconfig = ipconfig
       
       
    def infoAllVRAs(self):
        response = requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
        print(response)
        return response
       
    


