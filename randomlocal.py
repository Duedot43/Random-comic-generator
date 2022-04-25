import requests, json, os
def update_xkcd(folder_location):
    latest = open(str(folder_location) + "/latest", "r+")
    #lines = latest.readlines()
    latest_string = latest.read()
    latest_lists = latest_string.strip('][').split(', ')
    latest_list = []
    for x in latest_lists:
        latest_list.append(int(x))
    #latest_list = list(latest_list)
    res = requests.get("http://xkcd.com/info.0.json")
    jsoni = json.loads(res.text)
    if int(latest_list[int(int(len(latest_list))-1)]) < int(jsoni['num']):
        for x in range(int(latest_list[int(int(len(latest_list))-1)]),int(jsoni['num'])+1):
            if x != int(latest_list[int(int(len(latest_list))-1)]):
                get_num = requests.get(f"http://xkcd.com/{x}/info.0.json")
                jsone = json.loads(get_num.text)
                os.system(f"curl {jsone['img']} --output {folder_location}/{x}.png")
                latest_list.append(int(x))
        latest.seek(0) 
  
        # to erase all data 
        latest.truncate() 
        latest.write(str(latest_list))
        latest.close()


def random_xkcd(folder_location):
    pass
def update_gar(folder_location):
    pass
def random_gar(folder_location):
    pass
def random_all(xkcd_folder, gar_folder):
    pass
update_xkcd("./xkcd_comics")