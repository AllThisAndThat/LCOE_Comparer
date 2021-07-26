"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: main.py (main)
Description: To explore different energy sources and which can be
used to meet demand given constraints

TO-DO:
- Add GUI for data
- Add Gui to enter data
- Graph a hypothetical demand curve
- Add a carbon tax
- Add government subsidies
- Add a land tax
- Compare different sources
- Update test code
- Addapt style standard
"""

from energy_source import EnergySource, NonrenewableSource, RenewableSource
import data

def main():
    coal_plant = NonrenewableSource(**data.coal)
    natural_gas_plant = EnergySource(**data.natural_gas)
    onshore_wind_farm = RenewableSource(**data.onshore_wind)
    min_test_source = EnergySource(**data.min_test)

    # coal_plant.print_info()
    # natural_gas_plant.print_info()
    # onshore_wind_farm.print_info()
    # min_test_source.print_info()

    # coal_plant.print_fuel_info()
    # natural_gas_plant.print_fuel_info()
    # onshore_wind_farm.print_fuel_info()
    # min_test_source.print_fuel_info()

    # coal_plant.print_power_info()
    # natural_gas_plant.print_power_info()
    # onshore_wind_farm.print_power_info()
    # min_test_source.print_power_info()

    # coal_plant.print_cost_distribution_info(graph=True)
    # natural_gas_plant.print_cost_distribution_info(graph=True)
    # onshore_wind_farm.print_cost_distribution_info(graph=True)
    # min_test_source.print_cost_distribution_info(graph=True)

if __name__ == "__main__":
    main()