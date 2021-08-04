"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: data_csv.py (main)
Description: Retrieve source data from csv file.
"""

import csv

sources = []
with open('source_data.csv', 'r', encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # print(line, end='\n\n')
        for key in line.copy():
            # print(key,end=', ')
            if line.get(key) == '': # delete empty entities
                del line[key]
            elif line.get(key).isnumeric():  # Convert to int
                line[key] = int(line[key])
            elif line.get(key).replace('.', '', 1).isdigit(): # Convert to float
                line[key] = float(line[key])
       
        sources.append(line)

for source in sources:
    try:
        name = source['name'].lower()
        if  name == 'coal':
            coal = source
        elif name == 'natural gas':
            natural_gas = source
        elif name == 'advanced nuclear':
            advanced_nuclear = source
        elif name == 'onshore wind':
            onshore_wind = source
        elif name == 'rooftop solar pv':
            rooftop_solar = source
        else:
            raise ValueError(f"Unknown source error: '{name}' "
                "does not match database.")
    except ValueError as err:
        print(err)