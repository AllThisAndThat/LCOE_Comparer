from energy_source import EnergySource
import data

def main():
    coal_plant = EnergySource(**data.coal)
    natural_gas_plant = EnergySource(**data.natural_gas)
    onshore_wind_farm = EnergySource(**data.onshore_wind)
    # min_test_source = EnergySource(**data.min_test)
    empty_test_source = EnergySource(**data.empty_test)
    # zero_test_source = EnergySource(**data.zero_test)

    # coal_plant.print_input_properties()
    # natural_gas_plant.print_input_properties()
    # onshore_wind_farm.print_input_properties()
    # min_test_source.print_input_properties()
    # empty_test_source.print_input_properties()
    # zero_test_source.print_input_properties() 

    # coal_plant.print_all()
    # natural_gas_plant.print_all()
    # onshore_wind_farm.print_all()
    # min_test_source.print_all()
    empty_test_source.print_all()
    # zero_test_source.print_all()

    # EnergySource.Print_num_sources()

    # coal_plant.print_info()
    # natural_gas_plant.print_info()
    # onshore_wind_farm.print_info()
    # min_test_source.print_info()
    # empty_test_source.print_info()
    

    # coal_plant.print_fuel_info()
    # natural_gas_plant.print_fuel_info()
    # onshore_wind_farm.print_fuel_info()
    # min_test_source.print_fuel_info()
    # empty_test_source.print_fuel_info()

    # coal_plant.print_power_info()
    # natural_gas_plant.print_power_info()
    # onshore_wind_farm.print_power_info()
    # min_test_source.print_power_info()
    # empty_test_source.print_power_info()

    # coal_plant.print_cost_distribution_info(graph=True)
    # natural_gas_plant.print_cost_distribution_info(graph=True)
    # onshore_wind_farm.print_cost_distribution_info(graph=True)
    # min_test_source.print_cost_distribution_info(graph=True)
    # empty_test_source.print_cost_distribution_info(graph=True)

    # coal_plant.print_efficiency_info()
    # natural_gas_plant.print_efficiency_info()
    # onshore_wind_farm.print_efficiency_info()
    # min_test_source.print_efficiency_info()
    # empty_test_source.print_efficiency_info() 

    # EnergySource.print_all()

if __name__ == "__main__":
    main()