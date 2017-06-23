##########################################################################
## Imports
##########################################################################

import os
import json
import requests
from bs4 import BeautifulSoup
import re


##########################################################################
## Module Variables/Constants
##########################################################################
# BASIC VERSION
# ZILLOW_URL = 'https://www.zillow.com/homes/20001_rb/'
#
# response = requests.get(ZILLOW_URL)
#
# html_doc = response.text
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# test = soup.select(".zsg-photo-card-overlay-link")
#
# for item in test:
#     print(item)

# VERSION 1
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

for i in zips:
    print("\n", i, "\n", '----')
    for j in range(1,21):

        ZILLOW_URL = "https://www.zillow.com/homes/%s_rb/%s_p/" % (i,j)
        response = requests.get(ZILLOW_URL)
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        for item in soup.find_all(href=True):
            if '_zpid' in item['href']:
                zpids=((item['href'].split('/')[-2])[:-5])
                print(zpids)








##########################################################################
## Functions
##########################################################################

# def fetch_press_releases():
    # """
    # Performs a GET on the DOJ web service and return the array found in the
    # 'results' attribute of the JSON response
    # """
    # execute a GET request and store the results
    # response = requests.get(ZILLOW_URL)
    # response.status_code
    # decode as json and store the results

    # return the 'results' array of press releases
    #return data['results']


# def main():
    # """
    # Main execution function to perform required actions
    # """
    # fetch array of press releases
    #press_releases = fetch_press_releases()

    # iterate press releases
    #for release in press_releases:

        #path = './releases/%s.json' % release['uuid']
        #content = json.dumps(release)

        #f = open(path, 'wb')
        #f.write(content.encode('utf-8'))
        #f.close()
    # pass

##########################################################################
## Execution
##########################################################################

# if __name__ == '__main__':
#     main()
