# Legal Disclaimer:
#----------------------
#This script is an example script and is not supported under any Zerto support program or service.
#The author and Zerto further disclaim all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose.
#In no event shall Zerto, its authors or anyone else involved in the creation, production or delivery of the scripts be liable for any damages whatsoever (including, without
#limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or the inability
#to use the sample scripts or documentation, even if the author or Zerto has been advised of the possibility of such damages.  The entire risk arising out of the use or
#performance of the sample scripts and documentation remains with you.

#importing request, json
#importing HTTPBasicAuth library for ZVM basic authentication
import requests
from requests.auth import HTTPBasicAuth
import zvm
from secrets import zvm_ip, zvm_u, zvm_p

#Declaring Environment variables
base_url = "https://"+zvm_ip+":9669/v1"
session = base_url+"/session/add"

###Functions####
def login(session_url, zvm_user, zvm_password):
   returnDict = {'base_url': base_url}
   print("Getting ZVM API token...")
   auth_info = "{\r\n\t\"AuthenticationMethod\":1\r\n}"
   headers = {
     'Accept': 'application/json',
     'Content-Type': 'application/json'
   }
   response = requests.post(session_url, headers=headers, data=auth_info, verify=False, auth=HTTPBasicAuth(zvm_user, zvm_password))
   if response.ok:
      auth_token = response.headers['x-zerto-session']
      print("Api Token: " + auth_token)
      headers['x-zerto-session'] = auth_token
      print(headers)
      returnDict['headers'] = headers
      return returnDict

   else:
      print("HTTP %i - %s, Message %s" % (response.status_code, response.reason, response.text))



test = login(session, zvm_u, zvm_p)

testUrl = 'https://192.168.1.42:9669/v1'
testHeaders = test['headers']

#test2 = zvm.peersites('https://192.168.1.42:9669/v1', test['headers'])
#test2 = zvm.getAllVolumeInfo(test['headers'],test['base_url'])
#test3 = zvm.getLicenseNew(test['headers'],test['base_url'])

#test2 = login(session, zvm_u, zvm_p)
#test3 = login(session, zvm_u, zvm_p)


# TODO: Return entire header as opposed to just key

# TODO: Securely pass credentials without storing in memory

# TODO: Error handle 401, 403, etc.

