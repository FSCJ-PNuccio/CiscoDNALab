import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

BASE_URL = 'https://sandboxdnac.cisco.com'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = input('Enter username: ')
PASSWORD = getpass('Enter password: ')

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)

token = response.json()['Token']
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

DEVICES_URL = '/dna/intent/api/v1/network-device'

response_devices = requests.get(BASE_URL + DEVICES_URL, headers = headers, verify=False)

print(response_devices.json())
