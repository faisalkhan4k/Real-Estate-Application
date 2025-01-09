from bs4 import BeautifulSoup
import requests
from variables import all_area_list , set_of_all_area_list
import time
import random


import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/1.27.109"
}


BASE_URL = 'https://www.google.com/search?q='

longlat_area = dict()

for i in set_of_all_area_list:
    Search_line = f'{i} longitude and latitude'
    time.sleep(random.uniform(1, 5))  # Random delay between 1 to 5 seconds
    request_to_page= requests.get(BASE_URL+Search_line,headers=HEADERS)

    if request_to_page.status_code == 200:
        soup = BeautifulSoup(request_to_page.text , 'html.parser')
        latlong_div = soup.find('div',class_ = 'wvKXQ')
        try:
            print(latlong_div.text)
            longlat_area[i] = latlong_div.text
        except:
            print('sorry no content')
    else:
        print('error can\'t reach page')
    
print(longlat_area)