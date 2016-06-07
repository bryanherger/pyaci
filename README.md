# pyaci
An implementation of ACI API functionality to query HPE IDOL services.
This library is also able to extract entities from text using IDOL Eduction server.

SETUP
Edit idol/config.py to match your installation.

USAGE
pyaci_example.py shows some usage
Responses are returned as ElementTree as described at https://docs.python.org/2/library/xml.etree.elementtree.html

FEEDBACK
Please submit bugs and features via GitHub project page.

This code is derived from aci2csv at 
Original README:
# aci2csv
idol aci 2 csv in python

this is demo code, please use with care

example: to export data for a new month, or database create a new script by copying
the file may.py

edit the parameters in the function call

idol_query.query("1/5/2016","31/5/2016","SURVEY")


to specify:

parameter #1: FROM DATE
parameter #2: TO DATE
parameter #3: DATABASE IN IDOL

you can list/view the databases here:
http://10.210.148.80:9010/action=admin#page/databases

Also, ?f you need to ed?t the fields that are returned in the report you need to edit

idol_query.py

where this l?ne defines the fields / columns

  keys = ['GSM_NO','DREDATE','DREDBNAME','CATEGORYTAG','EMPCATEGORYTAG','SENTIMENT']

the ava?lable fields / columns are shown in the document meta v?ew in B?fHI

save the script with a new name e.g. june_survey_sentiment.py

to create the report, ?nvoke the new script us?ng the python interpreter e.g.

C:\...\> python june_survey_sentiment.py > june_survey_sentiment.txt

this will create a TAB separated file which you can then ?mport to Excel and v?ew as a spreadsheet




