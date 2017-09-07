# RealEstateMoguls
Real Estate Capstone Project

Both active listings and sold (last 90 days) listings are pulled as of 6/23/17.

Master For Sale ZPIDs.txt has 2887 records.
Master Sold ZPIDs.txt has 8781 records.

11,668 total records, we should only need to run GetDeepComps API call, with 25 comps, yielding 291,700 + 11,668 = 303,368 records

With a max of 3,000 API calls/day, will need to run for 4 days

Tables for additional features:-
-------------------------
license_summary_float --> growth yoy & yoy_5 in licenses per zipcode first 6 month data  each yr
lic_cat_crosstab_12m_yoy --> License categories as columns 12month data
lic_cat_crosstab_6m_yoy. --> License categories as columns 6month data
license_cat_12m_sumry_float --> All License categories as rows 12month data
license_cat_6m_sumry_float. --> All License categories as rows 6month data
zhvi. --> Zillow neighborhood data by zipcide for DC only
