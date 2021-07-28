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
    'f_o_and_m': 42.1,
    'v_o_and_m': 4.6,
    'fuel_cost': 1.95,
    'heat_rate': 8800,
    'capacity': 650,
    'capacity_factor': 0.475,
    'co2_rate': 95.23,
    'co2_tax': 0.005
}

natural_gas = {
    'name': 'Natural Gas',
    'capital_cost': 978,
    'f_o_and_m': 11,
    'v_o_and_m': 3.5,
    'fuel_cost': 3.95,
    'heat_rate': 6600,
    'capacity': 702,
    'capacity_factor': 0.568    
}

onshore_wind = {
    'name': 'Onshore Wind',
    'interest': 5,
    'year_num': 20,
    'capital_cost': 1877,
    'f_o_and_m': 39.7,
    'capacity': 100,
    'capacity_factor': 0.348    
}

min_test = {
    'name': 'Min Test',
    'capacity': 200,
    'capacity_factor': 0.22,
}

empty_test = {

}

zero_test = {
    'name': "Zero",
    'capital_cost': 0,
    'f_o_and_m': 0,
    'v_o_and_m': 0,
    'fuel_cost': 1.95,
    'heat_rate': 4000,
    'capacity': 100,
    'capacity_factor': 0.5 
}