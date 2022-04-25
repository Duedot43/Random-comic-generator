import os
import urllib.request
from datetime import date, timedelta
count = 0
list_images = []
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   _____  _____           _____  _____ ______   __  __ ______  #
#  |  __ \|  __ \    /\   |_   _|/ ____|  ____| |  \/  |  ____| #
#  | |__) | |__) |  /  \    | | | (___ | |__    | \  / | |__    #
#  |  ___/|  _  /  / /\ \   | |  \___ \|  __|   | |\/| |  __|   #
#  | |    | | \ \ / ____ \ _| |_ ____) | |____  | |  | | |____  #
#  |_|    |_|  \_/_/    \_|_____|_____/|______| |_|  |_|______| #
#                                                               #
#  Made by Anurag (https://github.com/wafflemelon)               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                                                             
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
# to get a date
def daterange(start, end):
    for x in range(int((end - start).days)):
        yield start + timedelta(x)


# to create a directory because it will be a mess if not organized
dir = "./gar_comics/"
if not os.path.exists(dir):
    os.makedirs(dir)


todays_date = date.today()

# this has to be set because garfield started on 1978/6/19
starting_date = todays_date.replace(year=1978, month=6, day=19)


for some_date in daterange(starting_date, todays_date):
    date_list = Convert(str(some_date.year))
    reqd_date = f"{str(date_list[2])+str(date_list[3])}{some_date.month:02}{some_date.day:02}"
    #http://images.ucomics.com/comics/ga/1978/ga780619.gif
    # image_url = f"https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/{some_date.year}/{some_date}.gif"
    # but will print "1" instead of "01"
    image_url = f"http://images.ucomics.com/comics/ga/{some_date.year}/ga{reqd_date}.gif"

    file = f"{dir}{str(reqd_date)}.gif"
    if not os.path.exists(file):
        #print(image_url)
        os.system(f"curl {image_url} --output ./gar_comics/{count}.gif")
        list_images.append(count)
        count = count+1
os.system(f"echo '{list_images}' >> ./gar_comics/latest")
print("All comics have been downloaded")
print("thanks for using")
