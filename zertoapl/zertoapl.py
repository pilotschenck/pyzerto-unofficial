import zerto_auth
from zvm import zvm
from vra import vra, vraObject
from vpg import vpgs, vpgSettings
import sys


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
        return vraObject(self.zvm_ip, self.session, self.datastore, self.host, self.network, self.cpu, self.ram, self.ip, self.subnet, self.gateway,self.hostpass, self.key )
    
    def createNewVraObject(self, datastore, host, network, cpu, 
    ram, ip, subnet, gateway, hostpass=None, key=True, VERBOSE=True):
        testDatastore = datastore
        returnObject = {
            "DatastoreIdentifier":None,
            "HostIdentifier":None,
            "HostRootPassword":hostpass,
            "MemoryInGb":ram,
            "NumOfCpus":cpu,
            "NetworkIdentifier":None,
            "UsePublicKeyInsteadOfCredentials": key,
            "PopulatePostInstallation":False,
            "VraNetworkDataApi":{
                "DefaultGateway": gateway,
                "SubnetMask": subnet,
                "VraIPAddress": ip,
                "VraIPConfigurationTypeApi":"Static"
                }
        }
        returnObject["DatastoreIdentifer"] = zvm(self.zvm_ip, self.session).getDatastoreGuid(testDatastore)
        returnObject["HostIdentifier"] = zvm(self.zvm_ip, self.session).getHostGuid('192.168.111.1')
 
        return returnObject
    def vpgs(self):
        return vpgs(self.zvm_ip, self.session, self.vpgid)

    def vpgsettings(self):
        return vpgSettings(self.zvm_ip, self.session, self.vpgid, self.vmid, 
        self.nicid, self.volumeid)

#z = zertoapl(sys.argv[1], sys.argv[2], sys.argv[3])
z = zertoapl("192.168.111.20", "administrator@vsphere.local", "Zertodata1!")
z.createNewVraObject('FreeNAS-Left-01', 'host', 'network', '2', '3', '192.168.111.12', '255.255.255.0', '192.168.111.254')

hostguid = z.zvm(self.).getHostGuid('192.168.111.1')

#print(z.zvm().getLicense().json())
#print(z.vra().infoAllVRAs().json())
#print(z.vpgs().getInfoAllVpgs().json())
#print(z.vpgsettings().getSettingsForSingleVpg().json())
