
import requests
import json
import urllib3
from getpass import getpass

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

#from config import DNAC_URL, DNAC_PASS, DNAC_USER

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_USER = input('Enter username: ')
DNAC_PASS = getpass('Enter password: ')
DNAC_URL = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def pprint(json_data):
    
    print(json.dumps(json_data, indent=4, separators=(' , ', ' : ')))


def get_dnac_jwt_token(dnac_auth):
    
    url = DNAC_URL + '/dna/system/api/v1/auth/token'
    header = {'content-type': 'application/json'}
    response = requests.post(url, auth=dnac_auth, headers=header, verify=False)
    response_json = response.json()
    dnac_jwt_token = response_json['Token']
    return dnac_jwt_token


dnac_token = get_dnac_jwt_token(DNAC_AUTH)
print('\n\nThe Cisco DNA Center Token is: \n\n', dnac_token, '\n\n')




