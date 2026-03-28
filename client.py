import requests

class APIClient:
    def __init__(self):
        self.base_url= "https://jsonplaceholder.typicode.com"

    def get(self, endpoint):
        return requests.get(self.base_url+endpoint)

    def post(self, endpoint,payload):
        return requests.post(self.base_url+endpoint,json=payload)