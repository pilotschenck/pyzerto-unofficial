"""
The zerto_auth.py module is the main authenticator script that must be run before any other API calls are accepted
by the target Zerto Virtual Manager or Zerto Cloud Appliance.
"""

import requests
from requests.auth import HTTPBasicAuth

def login(zvm_ip, zvm_user, zvm_password):
    """The login function returns a valid header, including an API token, that can then be passed to newly instansiated
    classes from other modules.

    The login function accepts three str-type inputs (IP addresss of ZVM/ZCA, username of ZVM/ZCA, and password of ZVM/
    ZCA) and returns a dict-type containing the valid headers for future API requests.
    """
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