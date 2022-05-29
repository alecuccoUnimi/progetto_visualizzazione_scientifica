import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

URL = "https://www.speedtest.net/global-index"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#print(soup)

paesiSito = soup.find_all("td", class_="country")
velocitaSito = soup.find_all("td", class_="speed")
paesi = []
velocita = []
for p in paesiSito:
    paesi.append(p.text.strip())
for v in velocitaSito :
    velocita.append(v.text.strip())

#mobile media (142), fixed media (181),  median mobile(142), median fixed (181)

mobile_mean = pd.Series(data=velocita[:142], index = paesi[:142])
fixed_mean = pd.Series(data=velocita[142:323], index = paesi[142:323])
mobile_median = pd.Series(data=velocita[324:465], index = paesi[324:465])
fixed_median = pd.Series(data=velocita[466:648], index = paesi[466:648])


mobile_mean.to_csv('mobile_mean.csv')
fixed_mean.to_csv('fixed_mean.csv')
mobile_median.to_csv('mobile_median.csv')
fixed_median.to_csv('fixed_median.csv')