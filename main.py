"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: main.py (main)
Description: To explore different energy sources and which can be
used to meet demand given constraints

TO-DO:
1. What is the actual power output of a plant +
2. Where does cost of a plant go +
3. Graph the data for 2 +
4. GUI to enter this data -
5. Graph demand curve and what resources fill need -
6. Add a carbon tax -
7. Add a land tax -
8. Comparison between sources -
9. Test Code +
10. Style standard -
11. Add to github +
"""

from energy_source import EnergySource, NonrenewableSource
import data

def main():
    coal_plant = NonrenewableSource(**data.coal)
    natural_gas_plant = EnergySource(**data.natural_gas)
    #onshore_wind_farm = EnergySource(**data.onshore_wind)

    # coal_plant.print_info()
    # natural_gas_plant.print_info()
    # onshore_wind_farm.print_info()

    # coal_plant.print_fuel_info()
    # natural_gas_plant.print_fuel_info()
    # onshore_wind_farm.print_fuel_info()

    # coal_plant.print_power_info()
    # natural_gas_plant.print_power_info()
    # onshore_wind_farm.print_info()
    
    coal_plant.print_cost_distribution_info(graph=True)
    natural_gas_plant.print_cost_distribution_info(graph=True)
    # onshore_wind_farm.print_info()

if __name__ == "__main__":
    main()