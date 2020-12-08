import zerto_auth
from zvm import zvm
from vra import vra
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

    def vpgs(self):
        return vpgs(self.zvm_ip, self.session, self.vpgid)

    def vpgsettings(self):
        return vpgSettings(self.zvm_ip, self.session, self.vpgid, self.vmid, self.nicid, self.volumeid)

#z = zertoapl(sys.argv[1], sys.argv[2], sys.argv[3])

#print(z.zvm().getLicense().json())
#print(z.vra().infoAllVRAs().json())
#print(z.vpgs().getInfoAllVpgs().json())
#print(z.vpgsettings().getSettingsForSingleVpg().json())