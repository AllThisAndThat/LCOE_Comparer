"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: main.py (main)
Description: To explore different energy sources and which can be
used to meet demand given constraints

TO-DO:
- Graph a hypothetical demand curve
- Compare different sources
- Adapt style standard
- Add GUI for data
- Add Gui to enter data
- Update test program
- Add sources to data with realistic values
"""

from energy_source import EnergySource
import data_csv

def main():
    EnergySource.set_industry(interest=8, loan_period=15)
    
    coal = EnergySource(**data_csv.coal)
    natural_gas = EnergySource(**data_csv.natural_gas)
    advanced_nuclear = EnergySource(**data_csv.advanced_nuclear)
    onshore_wind = EnergySource(**data_csv.onshore_wind)
    rooftop_solar = EnergySource(**data_csv.rooftop_solar)

    EnergySource.print_LCOE_comparison()

if __name__ == "__main__":
    main()