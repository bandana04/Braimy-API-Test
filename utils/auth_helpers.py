
import requests
import json
from utils.endpoints import *

class AuthActions:
    def __init__(self):
        self.base_url = "https://braimyapi-hxc3h7gwd8cna7aq.centralindia-01.azurewebsites.net"
        self.headers = {
            "Content-Type": "application/json",
                "Accept": "text/plain",
                "x-tenant-subdomain":"byjus"
        }
        with open('/home/bandana/Desktop/Automation/Braimy API Test/data/new_user.json', 'r') as f:
            json_payload = json.load(f)
        self.user = json_payload[0]
        self.endpoints = AuthEndpoints()

    def register_user(self):
        url = self.base_url + self.endpoints.register_user
        response = requests.post(url, headers=self.headers, json=self.user)
        return response

    def resend_otp(self):
        payload = {
            "phoneNumber" : self.user["phoneNumber"]
        }
        url = self.base_url + self.endpoints.resend_otp
        response = requests.post(url, headers=self.headers, json=payload)
        return response






