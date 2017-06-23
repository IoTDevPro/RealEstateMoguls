##########################################################################
## Imports
##########################################################################

import os
import json
import requests
from bs4 import BeautifulSoup
import re

zips = (20001,
20002,
20003,
20004,
20005,
20007,
20008,
20009,
20010,
20011,
20012,
20015,
20016,
20017,
20018,
20019,
20020,
20024,
20032,
20036,
20037)

rid = (66125,
66126,
66127,
66128,
66129,
66130,
66131,
66132,
66133,
66134,
66135,
66136,
66138,
66139,
66140,
66141,
66142,
66143,
66146,
66151,
66154,
66155)

for i in rid:
    print("\n", i, "\n", '--sold--')
    for j in range(1,21):

        ZILLOW_URL = "https://www.zillow.com/homes/recently_sold/Washington-DC-20001/%s_rid/90_days/" % (i)
        response = requests.get(ZILLOW_URL)
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        for item in soup.find_all(href=True):
            if '_zpid' in item['href']:
                zpids=((item['href'].split('/')[-2])[:-5])
                print(zpids)
