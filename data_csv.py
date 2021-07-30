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

    del_entity = []
    for line in csv_reader:
        for key in line.keys():
            if line.get(key) == '': # Save empty entities
                del_entity.append(key)
            elif line.get(key).isnumeric():  # Convert to int
                line[key] = int(line[key])
            elif line.get(key).replace('.', '', 1).isdigit(): # Convert to float
                line[key] = float(line[key])
        for entity in del_entity:
            line.pop(entity) # Remove empty entities
        del_entity.clear()
        sources.append(line)