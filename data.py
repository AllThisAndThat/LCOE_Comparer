"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: Data.py (data)
Description: Store data on on parameters of different energy sources
"""

coal = {
    'name': 'Coal',
    'interest': 10,
    'year_num': 35,
    'capital_cost': 3636,
    'F_O_and_M': 42.1,
    'V_O_and_M': 4.6,
    'fuel_price': 1.95,
    'heat_rate': 8800,
    'capacity': 650,
    'capacity_factor': 0.475
}

natural_gas = {
    'name': 'Natural Gas',
    'capital_cost': 978,
    'F_O_and_M': 11,
    'V_O_and_M': 3.5,
    # 'fuel_price': 3.95,
    # 'heat_rate': 6600,
    'capacity': 702,
    'capacity_factor': 0.568    
}

onshore_wind = {
    'name': 'Onshore Wind',
    'interest': 5,
    'year_num': 20,
    'capital_cost': 1877,
    'F_O_and_M': 39.7,
    'capacity': 100,
    'capacity_factor': 0.348    
}

min_test = {
    'name': 'test test test',
    'capacity': 200,
    'capacity_factor': 0.22,   
    'capital_cost': 1000
}