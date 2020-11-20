import requests
import urllib3
from secrets import vc_ip, zvm_u, zvm_p
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.vapi.std_client import DynamicID
session = requests.session()

# Disable cert verification for demo purpose. 
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server=vc_ip, username=zvm_u, password=zvm_p, session=session)

# List all VMs inside the vCenter Server
vmList = vsphere_client.vcenter.VM.list()

protectedTag = ''


def get_tag(tag_name):

    tags = vsphere_client.tagging.Tag.list()
    for tag in tags:
        t = vsphere_client.tagging.Tag.get(tag)
        if t.name == tag_name:
            return {
                "id": t.id,
                "category_id": t.category_id
            }

