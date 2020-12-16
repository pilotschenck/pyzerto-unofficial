import zerto_auth
from zvm import zvm
from vra import vra, vraObject
from vpg import vpgs, vpgSettings
import sys
import json


class zertoapl:
    def __init__(self, zvm_ip, zvm_user, zvm_password, vpgid=None, vmid=None, nicid=None, volumeid=None):
        self.session = zerto_auth.login(zvm_ip, zvm_user, zvm_password)
        self.zvm_ip = zvm_ip
        self.zvm_user = zvm_user
        self.zvm_password = zvm_password
        self.vpgid = vpgid
        self.vmid = vmid
        self.nicid = nicid
        self.volumeid = volumeid

    def zvm(self):
        return zvm(self.zvm_ip, self.session)

    def vra(self):
        return vra(self.zvm_ip, self.session)
    
    def vraObject(self):
        return vraObject(self.zvm_ip, self.session, self.datastore, self.host, self.network, self.ram, self.ip, self.subnet, self.gateway,self.hostpass, self.key )
    
    def createNewVraObject(self, datastore, host, network, 
    ram, ip, subnet, gateway, hostpass=None, key=True, VERBOSE=True):
        datastore_name = datastore
        host_name = host
        network_name = network
        returnObject = {
            "DatastoreIdentifier":None,
            "HostIdentifier":None,
            "HostRootPassword":hostpass,
            "MemoryInGb":ram,
            "NetworkIdentifier":None,
            "UsePublicKeyInsteadOfCredentials": key,
            "VraNetworkDataApi":{
                "DefaultGateway": gateway,
                "SubnetMask": subnet,
                "VraIPAddress": ip,
                "VraIPConfigurationTypeApi":"Static"
                }
        }
        returnObject["DatastoreIdentifier"] = zvm(self.zvm_ip, self.session).getDatastoreGuid(datastore_name)
        returnObject["HostIdentifier"] = zvm(self.zvm_ip, self.session).getHostGuid(host_name)
        returnObject["NetworkIdentifier"] = zvm(self.zvm_ip, self.session).getNetworkGuid(network_name)

        return json.dumps(returnObject)

    def vpgs(self):
        return vpgs(self.zvm_ip, self.session, self.vpgid)

    def vpgsettings(self):
        return vpgSettings(self.zvm_ip, self.session, self.vpgid, self.vmid, 
        self.nicid, self.volumeid)


