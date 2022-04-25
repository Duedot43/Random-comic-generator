import requests
import json
import os
def getval(file):
    res = requests.get("http://xkcd.com/" + file + "/info.0.json")
    if res.status_code == 200:
        p2 = str(res.text)
        return p2
os.makedirs("xkcd_comics")
res = requests.get("http://xkcd.com/info.0.json")
if res.status_code == 200:
    p2 = str(res.text)
jsont = json.loads(p2)
img_list = []

for x in range(1,jsont['num']):
    if x != 404:
        get = getval(str(x))
        jsont = json.loads(get)
        img_list.append(jsont['num'])
        os.system(f"curl '{jsont['img']}' --output ./xkcd_comics/{jsont['num']}.png")

with open('./xkcd_comics/latest', 'a') as f:
    f.write(str(img_list))