import argparse
from flattener import Flattener
import requests
import json
from requests.auth import HTTPBasicAuth
import getpass
            
def main():
    user = "dentello@hotmail.com"
    password = "brqnix4e5iqajzcgqlypxla7n26olany5utxvsausqkwbypqtmqq"
    
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "PreviewRun": "true"
    }
    URL = "https://pedentello.visualstudio.com/MyProject/_apis/pipelines/1/runs?api-version=7.1-preview"
    resp = requests.post(URL,headers=headers,data=json.dumps(data),auth=HTTPBasicAuth(user, password))
    if(resp.status_code == 200):
        print(resp.json()["finalYaml"])
    else:
        print(resp.text)

main()
