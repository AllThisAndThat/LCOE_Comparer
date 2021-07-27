"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: main.py (main)
Description: To explore different energy sources and which can be
used to meet demand given constraints

TO-DO:
- Add a print all sources function
- Add a print all parameters method
- Add GUI for data
- Add Gui to enter data
- Graph a hypothetical demand curve
- Add a carbon tax
- Add government subsidies
- Add a land tax
- Compare different sources
- Update test code
- Adapt style standard
"""

from energy_source import EnergySource
import data

def main():
    coal_plant = EnergySource(**data.coal)
    natural_gas_plant = EnergySource(**data.natural_gas)
    onshore_wind_farm = EnergySource(**data.onshore_wind)

    # EnergySource.Print_num_sources()


if __name__ == "__main__":
    main()