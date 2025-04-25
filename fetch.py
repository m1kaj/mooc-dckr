# -*- coding: utf-8 -*-

"""
Fetches the age distribution data from Finnish stat.fi open data API.

This function makes a GET request to the provided URL and parses the JSON response.
It is designed to be used with the pxdata API for Finnish population statistics.

The query used here is a POST request with a predefined query loaded from ./query.json.

Saves age distribution data in file ./age_distribution.csv
"""

import datetime
import requests
import json


QUERY_URL = "https://pxdata.stat.fi:443/PxWeb/api/v1/fi/StatFin/vaerak/statfin_vaerak_pxt_11rd.px"


# Requests library accepts data argument as a dictionary. We read the query from file.
with open('./query.json', 'r') as file:
    query = json.load(file)

# Set the headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Make a POST request to the API
response = requests.post(QUERY_URL, headers=headers, json=query)

# Check if the request was successful
if response.status_code != requests.codes.ok:
    raise Exception(f"Failed to fetch population data: {response.status_code}")

# Next we will parse the response JSON and build a dictionary. The values we want are
# returned in array or integers. Name of the array is "value". To find out which age
# group each integre in array corresponds to, we need to look at the "dimension" part
# of the response. The "dimension" part contains the age groups and their corresponding
# indices in the "value" array. We "cheat" here and use assumed knowledge of the returned
# JSON structure. 

resp = response.json()
age_dict = resp['dimension']['Ikä']['category']['label']

# Skip the first element which is "Yhteensä" (Total)
age_groups = list(age_dict.values())[1:]

# We take the same indices from "value" array
values = resp['value'][1:]

if len(age_groups) != len(values):
    raise Exception("Mismatch between age groups and values length")

# Create a dictionary to hold the age distribution data
age_distribution = {}
for i in range(len(age_groups)):
    age_distribution[age_groups[i]] = values[i]

# Save the age distribution data to a CSV file
ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('./age_distribution.csv', 'w') as file:
    file.write("Aikaleima,Ikä 31.12.2023,Määrä\n")
    for age_group, value in age_distribution.items():
        file.write(f"{ts},{age_group},{value}\n")
