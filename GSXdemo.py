import requests
import json

url = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

headers = {
    'Authorization': "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
    'Cache-Control': "no-cache",
    'Postman-Token': "2e7ff5b1-2699-473a-9b4d-8e815008c77b"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)

r_json = json.loads(response.text)
token = r_json["Token"]

url = "https://sandboxdnac.cisco.com/api/v1/network-device"

headers = {
    'x-auth-token': token,
    'Cache-Control': "no-cache",
    'Postman-Token': "de505fd5-e5d3-4675-a2dd-381bdb7144c6"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
