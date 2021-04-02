import os
import requests
import zipfile
import csv
import operator
import config

try:
    result = requests.get(config.DATASET_URL, steam =True)
    if result.status_code == 200:
        with open(config.ZIP_FILENAME, 'wb') as f:
            for chunk in result:
                f.write(chunk)
        with zipfile.ZipFile(config.ZIP_FILENAME, 'r') as zf:
            for zf_name in zf.namelist():
                if zf_name[-4:] == '.csv':
                    zf.extract(zf_name, '.')
                    os.rename(zf_name, config.CSV_FILENAME)
except(requests.RequestException):
    pass

bus_stops_street_count={}
bus_stops_admarea_count={}

with open('bus_stops.csv', 'r', encoding='windows-1251') as f:
    fields
