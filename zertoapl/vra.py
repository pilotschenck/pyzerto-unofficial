"""
The vra.py module contains properly-formatted API calls for VRA related tasks. The
tasks can include installing a vra, uninstalling a vra, editing a VRA, or upgrading
a vra
"""

import json 
import requests
#from zerto_auth import testUrl, testHeaders
class vra():
    """
    The VRA class houses VRA specific methods
    ...
    Attributes
    ----------
    zvmurl : str
        the IP address of the target ZVM

    headerwithkey : dict
        a properly formatted dict containing the following key:value pairs:
        {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            'x-zerto-session': str-type containing valid session key generated with zerto_auth.py
        }
    
    vra_id: str 
        unique identifier for individual VRA 

    vra_dict: dict
        dictionary object for VRA inputs 

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
        Uninstall individual VRA
    """
    endPoint = '/vras'
    
    def __init__(self, zvmip, headerwithkey):
        """
        Parameters
        ----------
        zvmip : str
            The IP of the ZVM or ZCA
        headerwithkey : dict
            A properly formatted dict containing the following key:value pairs:
                {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                    'x-zerto-session': str-type containing valid session key generated with zerto_auth.py
                }
        """

        self.zvmurl = 'https://' + zvmip + ':9669/v1'
        self.headerwithkey = headerwithkey 
       
    def infoAllVRAs(self):
        """
        Returns information on all VRAs
        
        Returns
        -------
        type requests.models.Response object
        """        
        return requests.get(self.zvmurl + self.endPoint, headers=self.headerwithkey, verify=False)
 
    def upgradeGroupVRAs(self, vra_id):
        """
                Upgrade a group of VRAs which are specified in the vra_id body

        Parameters
        ----------
        vra_id: dict , required
            A properly formatted dict containing the following key:value pairs:
            {  
                "VraIdentifiers":
                [  
                    "String content",
                    "String content",
                    ...
                    "String content"
                ]
            }

        Returns
        -------
        type requests.models.Response object
        """    
        return requests.post(self.zvmurl + self.endPoint + "/upgrade", headers=self.headerwithkey, data=vra_id, verify=False)
  
    def upgradeVRA(self, vra_id):
        """
        Upgrade individual VRA
        
        Parameters
        ----------
        vra_id: str, required
            the unique identifier for the vra requiring upgrade

        Returns
        -------
        type requests.models.Response object
        """        
        return requests.post(self.zvmurl + self.endPoint +"/" + vra_id + "/upgrade", headers=self.headerwithkey, verify=False)

    def installVRA(self, vra_dict):
        """
        Performs installation of a VRA

        Parameters
        ----------
        vra_dict: dict , required
            A properly formatted dict containing the following key:value pairs:
            {  
                "DatastoreIdentifier": "String content",
                "GroupName": "String content",
                "HostIdentifier": "String content",
                "HostRootPassword": "String content",
                "MemoryInGb":2,
                "NumOfCpus":1,
                "NetworkIdentifier": "String content",
                "UsePublicKeyInsteadOfCredentials": Boolean,
                "PopulatePostInstallation": Boolean,
                "VraNetworkDataApi": {  
                    "DefaultGateway": "String content",
                    "SubnetMask": "String content",
                    "VraIPAddress": "String content",
                    "VraIPConfigurationTypeApi": "String content"
                }
            }

        Returns
        -------
        type requests.models.Response object
        """ 
        return requests.post(self.zvmurl + self.endPoint, headers=self.headerwithkey, data=vra_dict, verify=False)

    def editVRA(self, vra_dict, vra_id):
        """
        Edit exiting VRA

        Parameters
        ----------
        vra_dict: dict , required
        {  
            "GroupName": "String content",
            "HostRootPassword": "String content",
            "UsePublicKeyInsteadOfCredentials": Boolean,
            "VraNetworkDataApi": {  
                "DefaultGateway": "String content",
                "SubnetMask": "String content",
                "VraIPAddress": "String content",
                "VraIPConfigurationTypeApi": "String content"
            }
        }

        vra_id: str, required
            the unique identifier for the vra requiring edit

        Returns
        -------
        type requests.models.Response object
        """         

        return requests.put(self.zvmurl + self.endPoint +"/" + vra_id, headers=self.headerwithkey, data=vra_dict, verify=False)
    
    def delVRA(self, vra_id):
        """
        Uninstall individual VRA
        
        Parameters
        ----------
        vra_id: str, required
            the unique identifier for the vra requiring uninstall

        Returns
        -------
        type requests.models.Response object
        """   
        return requests.delete(self.zvmurl + self.endPoint +"/" + vra_id, headers=self.headerwithkey, verify=False)



