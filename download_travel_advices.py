import requests
import urllib.request
from tqdm import tqdm
from bs4 import BeautifulSoup
import random
import re
import os
import time
import warnings
import cv2
import numpy as np

warnings.filterwarnings("ignore")

## Get all countries that have a travel advice
url_with_all_countries = "https://www.nederlandwereldwijd.nl/help/in-welke-taal-communiceert-welk-land"
r = requests.get(url_with_all_countries)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')
all_countries = soup.select("a[href*=\/landen\/]")

list_of_kaarten = os.listdir('original_maps/')


for i in tqdm(all_countries):
    country_url = i["href"] + "/reizen/reisadvies"
    if not country_url.startswith("https://www.nederlandwereldwijd.nl"):
        country_url = "https://www.nederlandwereldwijd.nl" + country_url
        
    # Change name of macedonia
    if "macedonie" in country_url and not "noord-macedonie" in country_url:
        country_url = country_url.replace("macedonie","noord-macedonie")
        
    # Look for travel advice image on the page
    r = requests.get(country_url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'lxml')
    image_url = soup.select_one("img[src*=reisadviezen][src*=png]")
    image_url = image_url["src"]
    
    # Skip if no image was found
    if image_url ==None:
        print("No map found for: " + country_url)
        continue
        
    
    
    ## Get the date when it was last changed
    date = re.findall("Laatst gewijzigd op:&nbsp;(\d\d-\d\d-\d\d\d\d)", html_content)[0]
    year = date[-4:]
    month = date[3:5]
    day = date[:2]
    
    if "_" not in image_url:
        print("No map found for: " + country_url)
        continue
    
    country_name = image_url.split('/')[-1].split('_')[1]
    files_of_country = [x for x in list_of_kaarten if country_name+"_" in x]
    targeturl = "original_maps/"+country_name+'_'+year+month+day+".png"
    
    # Check if the most recent file in the folder is not the same as the online version
    if len(files_of_country) > 0:
        last_file = max(files_of_country)
        with open(targeturl[8:], 'wb') as f:
            resp = requests.get("https://www.nederlandwereldwijd.nl"+image_url, verify=False)
            f.write(resp.content)
        online = cv2.imread(targeturl[8:])
        last = cv2.imread("original_maps/" + last_file)
        os.remove(targeturl[8:])
        if online.shape == last.shape:
            difference = cv2.subtract(online, last)        
            b, g, r = cv2.split(difference)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                continue
                
    # Download image if it does not exist yet
    if not targeturl[8:] in list_of_kaarten:
        with open(targeturl, 'wb') as f:
            resp = requests.get("https://www.nederlandwereldwijd.nl" + image_url, verify=False)
            f.write(resp.content)
