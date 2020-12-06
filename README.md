# pyzerto-unofficial
![Zerto Automation API Library Logo!](https://github.com/pilotschenck/pyzerto-unofficial/blob/main/zertoautomationapilibrary-logo.png?raw=true)

## Overview

pyzerto-unofficial is a simple python3 API wrapper for the Zerto product by the eponymous corporation. It is intended to 
simplify the deployment and management of Zerto in a code-driven manner. Potential uses for this API wrapper are as
diverse as you may wish to make it. An example script of automatically protecting tagged virtual machines (VMs) is
included in this library.

## Motiviation and Audience

The official Zerto API is a REST-driven architecture. This wrapper was developed to reduce the barrier of entry for
anyone interested in automating Zerto tasks via Python by abstracting the effort of generating a session key, 
constructing correctly formatted CRUD requests, and identifying the correct URL endpoints for any given API call. This
can benefit new Zerto users, Zerto partners deploying at-scale environments, and anyone with a Python and Zerto
background. 

## Disclaimer

This is not an official Zerto product in any way, shape, or form. Support is community-driven and you should thoroughly
test your scripts to ensure that you do not break anything by utilizing pyzerto-unofficial. In other words, don't blame
us if it messes something up!!

## Usage

### Installation

This package can be installed directly from PyPi or via git.

```shell
> pip install zertoapl
> pip install git+https://github.com/pilotschenck/pyzerto-unofficial.git#master
```

### The Zerto API, explained

The Zerto Virtual Manager (or Zerto Cloud Appliance) acts as the management plane for all things Zerto-related in your
environment. To use the Zerto API, you will need:
* The IP address of your target ZVM or ZCA and access from the machine running the Python library over TCP port 9669
* Credentials of a valid admin-level account for your ZVM or ZCA. For a ZVM, this usually means an admin- or nearly-
admin level vCenter account, and for a ZCA, this is usually the Administrator account of the underlying Windows instance 
or VM in AWS or Azure.

Using the IP address of the ZVM/ZCA and a valid user account, you can generate an API session token, which will then
need to be passed back to the ZVM/ZCA in the form of a properly formed header as well as a request body, if applicable, 
in order to run API calls to do interesting things like get local site information, create a virtual protection group 
(VPG) object, add VMs to said VPG, and so on. Furthermore, the ZVM/ZCA must have a valid license key installed in order 
to successfully run API calls (except for generating an API session token and applying a license!)

### Using the wrapper

Start by executing zerto_auth.py. The function `login` accepts three arguments: `zvm_ip`, `zvm_user`, and 
`zvm_password`. This function will return a `dict` with the properly formatted headers for running API commands against
the ZVM/ZCA, including a valid session token.

From here, you can instansiate classes which can be found in `zvm.py`, `vra.py`, and `vpg.py` modules. The theory behind
how the modules (and subsequent classes) were organized was based on the Zerto "object" that you would want to do
interesting things to. For example, if you want to get information about datastores visible to the ZVM, you will find
that method located in the `zvm` class under the `zvm` module. If you want to install or delete a VRA, you will find
`installVra` and `delVra` in the `vra` class under the `vra` module. Even though all API calls are executed against a
ZVM or ZCA, this modularization is intended to make sense to an admin.

#### A special note on Virtual Protection Groups

Virtual Protection Groups, or VPGs, require some specific clarification. To create and manage VPGs, you need to first
create a "VPG Object", to which you will then add VMs and specify specific instructions such as length of journal,
networks to attach do during a live failover or a test failover, and the like. However, none of your changes will be
applied unless and until you *commit* the settings.

One a VPG has been committed, the vpgSettings identifier *goes away*. Do not confuse the VPG identifier with a
vpgSettings identifier; these are two different things. Roughly speaking, you can think of the `vpgs` class in the `vpg`
module as anything having to do with existing VPG "containers" as a whole, and the `vpgSettings` class in the `vpg`
module as having to do with what's *inside* a VPG (with the exception of creating a VPG to begin with).

### Example: Adding a license

```python
from zertoapl.zerto import zvm
from zertoapl.zerto_auth import login

vczvmSession = login('10.0.10.50', 'zertoadmin@example.local', 'password')
z = zvm('10.0.10.50, vczvmSession')
z.addLicense('VALIDZERTOLICENSEKEYHERE')
```
    
### Example: Installing a VRA

```python
import json
from zertoapl.vra import vra
from zertoapl.zerto_auth import login

vczvmSession = login('10.0.10.50', 'zertoadmin@example.local', 'password')
v = vra('10.0.10.50', vczvmSession)
testVra = json.dumps({
            "DatastoreIdentifier": "GUID-OF-VCENTER.DATASTOREMOREF",
            "HostIdentifier": "GUID-OF-VCENTER.HOSTMOREF",
            "HostRootPassword": "ESXIPASSWORD",
            "MemoryInGb": 3,
            "NumOfCpus": 1,
            "NetworkIdentifier": "GUID-OF-VCENTER.NETWORKMOREF",
            "UsePublicKeyInsteadOfCredentials": False,
            "PopulatePostInstallation": False,
            "VraNetworkDataApi": {
                "DefaultGateway": "192.168.1.1",
                "SubnetMask": "255.255.255.0",
                "VraIPAddress": "192.168.1.90",
                "VraIPConfigurationTypeApi": "Static"
                }
            })
            
v.installVRA(testVra)
```

### Example: Pairing a site with another site
    
```python
import json, requests
from zertoapl.zerto_auth import login
from zertoapl.zvm import zvm

vczvmSession = login('10.0.10.50', 'zertoadmin@example.local', 'password')
awszcaSession = login('172.16.20.21', 'Administrator', 'password')
zvmOnsite = zvm('10.0.10.50', vczvmSession)
zcaInCloud = zvm('172.16.20.21', awszcaSession)
zcaTokenObject = zcaInCloud.generatePeeringToken()
zcaTokenActual = zcaTokenObject.json().get('Token')
pairOutput = requests.post('https://10.0.10.50:9669/v1/peersites',
                           headers=vczvmSession,
                           data=json.dumps({"HostName": '172.16.20.21', 
                                            "Port":"9071",
                                            "Token":zcaTokenActual}),
                           verify=False)
```
### Example: Create a VPG

```python
import json
from zertoapl.zerto_auth import login
from zertoapl.vpg import vpgSettings

vczvmSession = login('10.0.10.50', 'zertoadmin@example.local', 'password')
v = vpgSettings(zvm_ip, vczvmSession)

vpgPayload = json.dumps({
    "Basic": {
        "JournalHistoryInHours": 2,
        "Name": "TestVpg",
        "Priority": "Medium",
        "ProtectedSiteIdentifier": "IDENTIFIER1",
        "RecoverySiteIdentifier": "IDENTIFIER2",
        "RpoInSeconds": 600,
        "ServiceProfileIdentifier":  null,
        "TestIntervalInMinutes": 0,
        "UseWanCompression": "True",
        "ZorgIdentifier": null
    },
    "BootGroups": {
        "BootGroups": [
            {
                "BootDelayInSeconds": 0,
                "BootGroupIdentifier": "00000000-0000-0000-0000-000000000000",
                "Name": "Default"
            }
        ]
    },
    "Journal": {
        "DatastoreIdentifier": "GUIDOFVCENTER.DATASTOREMOREF",
        "Limitation": {
            "HardLimitInMB": 0,
            "HardLimitInPercent": 0,
            "WarningThresholdInMB": 0,
            "WarningThresholdInPercent": 0
        }
    },
    "LongTermRetention": null,

    "Networks": {
        "Failover": {
            "Hypervisor": {
                "DefaultNetworkIdentifier": "GUIDOFVCENTER.NETWORKMOREF"
            }
        },
        "FailoverTest": {
            "Hypervisor": {
                "DefaultNetworkIdentifier": "GUIDOFVCENTER.NETWORKMOREF"
            }
        }
    },
    "Recovery": {
        "DefaultDatastoreClusterIdentifier": null,
        "DefaultDatastoreIdentifier": "GUIDOFVCENTER.DATASTOREMOREF",
        "DefaultFolderIdentifier": "GUIDOFVCENTER.FOLDERMOREF",
        "DefaultHostClusterIdentifier": null,
        "DefaultHostIdentifier": "GUIDOFVCENTER.HOSTMOREF",
        "ResourcePoolIdentifier": null
    },
    "Scripting": {
        "PostRecovery": {
            "Command": null,
            "Parameters": null,
            "TimeoutInSeconds": 0
        },
        "PreRecovery": {
            "Command": null,
            "Parameters": null,
            "TimeoutInSeconds": 0
        }
    },
    "Vms": []
})
    
vpgSettingsId = v.createNewVpgSettingsObject(vpgPayload)
v.commitSettingsObject(vpgSettingsId)
```

## Acknowledgements

I would like to acknowledge several people for assisting, either directly or indirectly, in the creation of this
library. Shaun Finn directly contributed to the zerto_auth and vra modules, and Wes Carroll provided insight and 
assistance based on his experiences designing and developing his excellent PowerShell API wrapper. I would also like
to acknowledge Nick Costigan, Jacob Lucas and Chris Pacejo in providing their insight as professional developers.
