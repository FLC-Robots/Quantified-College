import requests
import json

class sensor():
    def __init__(self, member_id):
        self.member_id = member_id
        self.keyR = "ADE813DD-C8D2-11ED-B6F4-42010A800007"
        self.group_index = 1684
    
    def get_current_data(self, fields=None):
        fields = "temperature,humidity" if fields is None else fields
        url = f"https://api.purpleair.com/v1/groups/{self.group_index}/members/{self.member_id}?api_key={self.keyR}&fields={fields}"
        req = requests.get(url)
        data = json.loads(req.content)
        return data