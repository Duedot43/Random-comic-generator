import requests
import json
import os
def getval(file):
    res = requests.get("http://xkcd.com/" + file + "/info.0.json")
    if res.status_code == 200:
        p2 = str(res.text)
        return p2
os.makedirs("xkcd_comics")
get = getval("1")
jsont = json.loads(get)
print(jsont['img'])
