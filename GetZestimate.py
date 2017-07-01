##########################################################################
## Imports
##########################################################################

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import pandas as pd
import time
from datetime import date

# Remember to change the filename
readfile = open("ZPID2.txt", "r")

a=[]

for line in readfile:
    ids = line.split(",")
    ids2 = [x.replace('\t','').replace('\r','').replace('"','').replace('\n','') for x in ids]
    ids3 = (ids2[0])
    # print(ids3)

    # API_CALL: remember to replace with your zws-id
    API_CALL = "http://www.zillow.com/webservice/GetDeepComps.htm?zws-id=X1-ZWz1fsrxuqszkb_1y8f9&zpid=%s&count=25" % (ids3)

    response = requests.get(API_CALL)

    a.append(response.text)
    rcontent = response.content

def timeIzNow():
    '''
    returns current date as a string
    '''
    now = date.today()
    full = "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)

    return full

fileN = "Darius" # Change to your name

with open(fileN + timeIzNow() + ".txt", 'w') as f:
    for item in a:
        f.write("{}\n".format(item))
