from bs4 import BeautifulSoup
import csv
import bleach
import pandas as pd
import numpy as np
import regex as re

# read in all properties into a list
dates = ("Darius-8-2-2017.txt",
"Darius-8-3-2017.txt",
"Darius-8-4-2017.txt",
"Darius-8-5-2017.txt")

df2=pd.DataFrame(columns=['princomp','zpid', 'street', 'city', 'state', 'zipcode', 'latitude', 'longitude', 'taxAssessmentYear', 'taxAssessment', 'yearBuilt', 'lotSizeSqFt', 'finishedSqFt', 'bathrooms',
'bedrooms', 'lastSoldDate', 'lastSoldPrice', 'amount', 'lastupdated', 'valueChange', 'low', 'high', 'percentile'])

for i in dates:
    f = open(i, "r")
    x = f.readlines()
    home=[]
    home2=[]

    for index in range(len(x)):

        soup = BeautifulSoup(x[index], 'xml')

        if soup.find('principal') is not None:

            for item in soup.find('principal'):
                princomp = "prin"
                zpid = soup.find('zpid')
                street = soup.find('street')
                city = soup.find('city')
                state = soup.find('state')
                zipcode = soup.find('zipcode')
                latitude = soup.find('latitude')
                longitude = soup.find('longitude')
                taxAssessmentYear = soup.find('taxAssessmentYear')
                taxAssessment = soup.find('taxAssessment')
                yearBuilt = soup.find('yearBuilt')
                lotSizeSqFt = soup.find('lotSizeSqFt')
                finishedSqFt = soup.find('finishedSqFt')
                bathrooms = soup.find('bathrooms')
                bedrooms = soup.find('bedrooms')
                lastSoldDate = soup.find('lastSoldDate')
                lastSoldPrice = soup.find('lastSoldPrice')
                amount = soup.find('amount')
                lastupdated = soup.find('last-updated')
                valueChange = soup.find('valueChange')
                low = soup.find('low')
                high = soup.find('high')
                percentile = soup.find('percentile')
                zindexValue = soup.find('zindexValue')
                zindexOneYearChange = soup.find('zindexOneYearChange')

                prin = [(princomp),
                        (zpid),
                        (street),
                        (city),
                        (state),
                        (zipcode),
                        (latitude),
                        (longitude),
                        (taxAssessmentYear),
                        (taxAssessment),
                        (yearBuilt),
                        (lotSizeSqFt),
                        (finishedSqFt),
                        (bathrooms),
                        (bedrooms),
                        (lastSoldDate),
                        (lastSoldPrice),
                        (amount),
                        (lastupdated),
                        (valueChange),
                        (low),
                        (high),
                        (percentile)]

            home.append(prin)
            df=pd.DataFrame.from_records(home)
            df.columns=['princomp','zpid', 'street', 'city', 'state', 'zipcode', 'latitude', 'longitude','taxAssessmentYear', 'taxAssessment', 'yearBuilt', 'lotSizeSqFt', 'finishedSqFt', 'bathrooms',
            'bedrooms', 'lastSoldDate', 'lastSoldPrice', 'amount', 'lastupdated', 'valueChange', 'low', 'high', 'percentile']
            print(df.shape)

    df2=df2.append(df)
    print(df2.shape)

df2['zpid'] = df2['zpid'].astype('str')
df2['street'] = df2['street'].astype('str')
df2['city'] = df2['city'].astype('str')
df2['state'] = df2['state'].astype('str')
df2['zipcode'] = df2['zipcode'].astype('str')
df2['latitude'] = df2['latitude'].astype('str')
df2['longitude'] = df2['longitude'].astype('str')
df2['taxAssessmentYear'] = df2['taxAssessmentYear'].astype('str')
df2['taxAssessment'] = df2['taxAssessment'].astype('str')
df2['yearBuilt'] = df2['yearBuilt'].astype('str')
df2['lotSizeSqFt'] = df2['lotSizeSqFt'].astype('str')
df2['finishedSqFt'] = df2['finishedSqFt'].astype('str')
df2['bathrooms'] = df2['bathrooms'].astype('str')
df2['bedrooms'] = df2['bedrooms'].astype('str')
df2['lastSoldDate'] = df2['lastSoldDate'].astype('str')
df2['lastSoldPrice'] = df2['lastSoldPrice'].astype('str')
df2['amount'] = df2['amount'].astype('str')
df2['lastupdated'] = df2['lastupdated'].astype('str')
df2['valueChange'] = df2['valueChange'].astype('str')
df2['low'] = df2['low'].astype('str')
df2['high'] = df2['high'].astype('str')
df2['percentile'] = df2['percentile'].astype('str')


df2['zpid'] = df2['zpid'].replace(regex=True,to_replace=r'<zpid>|</zpid>',value="")
df2['street'] = df2['street'].replace(regex=True,to_replace=r'<street>|</street>',value="")
df2['city'] = df2['city'].replace(regex=True,to_replace=r'<city>|</city>',value="")
df2['state'] = df2['state'].replace(regex=True,to_replace=r'<state>|</state>',value="")
df2['zipcode'] = df2['zipcode'].replace(regex=True,to_replace=r'<zipcode>|</zipcode>',value="")
df2['latitude'] = df2['latitude'].replace(regex=True,to_replace=r'<latitude>|</latitude>',value="")
df2['longitude'] = df2['longitude'].replace(regex=True,to_replace=r'<longitude>|</longitude>',value="")
df2['taxAssessmentYear'] = df2['taxAssessmentYear'].replace(regex=True,to_replace=r'<taxAssessmentYear>|</taxAssessmentYear>',value="")
df2['taxAssessment'] = df2['taxAssessment'].replace(regex=True,to_replace=r'<taxAssessment>|</taxAssessment>',value="")
df2['yearBuilt'] = df2['yearBuilt'].replace(regex=True,to_replace=r'<yearBuilt>|</yearBuilt>',value="")
df2['lotSizeSqFt'] = df2['lotSizeSqFt'].replace(regex=True,to_replace=r'<lotSizeSqFt>|</lotSizeSqFt>',value="")
df2['finishedSqFt'] = df2['finishedSqFt'].replace(regex=True,to_replace=r'<finishedSqFt>|</finishedSqFt>',value="")
df2['bathrooms'] = df2['bathrooms'].replace(regex=True,to_replace=r'<bathrooms>|</bathrooms>',value="")
df2['bedrooms'] = df2['bedrooms'].replace(regex=True,to_replace=r'<bedrooms>|</bedrooms>',value="")
df2['lastSoldDate'] = df2['lastSoldDate'].replace(regex=True,to_replace=r'<lastSoldDate>|</lastSoldDate>',value="")
df2['lastSoldPrice'] = df2['lastSoldPrice'].replace(regex=True,to_replace=r'<lastSoldPrice currency="USD">|<lastSoldPrice>|</lastSoldPrice>',value="")
df2['amount'] = df2['amount'].replace(regex=True,to_replace=r'<amount currency="USD">|<amount>|</amount>',value="")
df2['lastupdated'] = df2['lastupdated'].replace(regex=True,to_replace=r'<last-updated>|</last-updated>|<lastupdated>|</lastupdated>',value="")
df2['valueChange'] = df2['valueChange'].replace(regex=True,to_replace=r'<valueChange/>|<valueChange currency="USD" duration="30">|<valueChange>|</valueChange>',value="")
df2['low'] = df2['low'].replace(regex=True,to_replace=r'<low currency="USD">|<low>|</low>',value="")
df2['high'] = df2['high'].replace(regex=True,to_replace=r'<high currency="USD">|<high>|</high>',value="")
df2['percentile'] = df2['percentile'].replace(regex=True,to_replace=r'<percentile>|</percentile>',value="")

df2.to_csv('Darius Week5.csv', encoding='utf-8', index=False, header=True)
