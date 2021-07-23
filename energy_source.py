"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: energy_source.py (class)
Content: EnergySource, NonrenewableSource
Description: Store classes relating to energy sources
"""

import matplotlib.pyplot as plt

class EnergySource:
    """
    Derives properties of energy sources from given properties
    
    Attributes:
    interest - the interest or discount rate as a percentage
    i - the interest as a decimal
    year_num and n - lifetime of powerplant
    CRF - capital recovery factor (1/yr)
    capital_cost - initial cost for a given capacity ($/kW)
    F_O_and_M - fixed operation and maintaince cost ($/kW-yr)
    V_O_and_M - variable operation and maintaince cost ($/MWh)
    capacity - maximum capacity of the power plant (MWh)
    capacity_factor - actual / capacity (unitless)
    LCOE - the levelized cost of energy ($/MWh)
    num_of_sources - recond of instances
    capital_term - capital cost after conversion ($/kWh)
    fixed_term - fixed O&M after conversion ($/kWh)
    variable_term - variable O&M after conversion ($/kWh)
    """
    num_of_sources = 0
    Industry_I = 5
    Industry_N = 20

    def __init__(self, *, name, capacity, capacity_factor,
                 interest=Industry_I, year_num=Industry_N,
                 capital_cost=0, F_O_and_M=0, V_O_and_M=0):
        """Set variables and derive properties."""
        self.name = name
        self.i = interest / 100
        self.n = year_num

        self.capital_cost = capital_cost
        self.F_O_and_M = F_O_and_M
        self.V_O_and_M = V_O_and_M

        self.capacity = capacity
        self.capacity_factor = capacity_factor

        self.calc_CRF()
        self.calc_LCOE()

        EnergySource.num_of_sources += 1

    def calc_CRF(self):
        """Calculate the CRF based on interest and annuity."""
        self.CRF = ((self.i * (1 + self.i)**self.n) 
                / (((1 + self.i)**self.n) - 1))

    def calc_LCOE(self):
        """Calculate LCOE based on variety of costs."""
        HOURS_PER_YEAR = 8760
        KWH_PER_MWH = 1000
        self.capital_term = ((self.capital_cost * self.CRF) 
                           / (HOURS_PER_YEAR * self.capacity_factor))
        self.fixed_term = (self.F_O_and_M 
                        / (HOURS_PER_YEAR * self.capacity_factor))
        self.variable_term = self.V_O_and_M / KWH_PER_MWH
        self.LCOE_kWh = (self.capital_term 
                       + self.fixed_term 
                       + self.variable_term)
        self.LCOE = self.LCOE_kWh * KWH_PER_MWH


    def print_info(self):
        """Print general information of source."""
        print('-' * 70)
        print(f"General Information of '{self.name}' source")
        print(f'Capacity: {self.capacity} MW')
        print(f'Capacity Factor: {self.capacity_factor}')
        print(f'Used capital recovery factor: {round(self.CRF, 3)}')
        print(f'Levelized Cost ${round(self.LCOE, 2)}/MWh')
        print('-' * 70)

    def print_power_info(self):
        """Print power properties of source."""
        print('-' * 70)
        print(f"Power Information of '{self.name}' source")
        print(f'Total capacity: {self.capacity} MW')
        print(f'Capacity factor: {self.capacity_factor}')
        print(f'Actual average power: '
              f'{round(self.capacity * self.capacity_factor, 2)} MW')
        print('-' * 70)


    def print_cost_distribution_info(self, *, graph=False):
        print('-' * 70)
        print(f"Cost Distribution Information of '{self.name}' source")
        print(f'Capital term: '
            f'{round((self.capital_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Fixed term: '
            f'{round((self.fixed_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Variable term: '
            f'{round((self.variable_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Total LCOE: ${round(self.LCOE, 2)}/MWh')
        print('-' * 70)

        if graph:
            labels = ('Capital Term', 'Fixed Term', 'Variable Term')
            sizes = [self.capital_term, self.fixed_term,
                     self.variable_term]
            colors = ['orange', 'yellowgreen', 'lightcoral']
            plt.pie(sizes, colors=colors, autopct='%1.1f%%',
                    pctdistance=1.15, startangle=140, normalize=True)
            plt.legend(labels, loc="best")
            plt.axis('equal')
            plt.show()


class NonrenewableSource(EnergySource):
    '''
    Describes and derives properties of nonrenewable sources.
    
    Attributes:
    fuel_price - cost for fuel ($/mmBTU)
    heat_rate - measure of efficiency (BTU/kwh)
    '''
    Industry_I = EnergySource.Industry_I
    Industry_N = EnergySource.Industry_N

    def __init__(self, *, name, capacity, capacity_factor, heat_rate,
                 interest=Industry_I, year_num=Industry_N,
                 capital_cost=0, F_O_and_M=0, V_O_and_M=0,
                 fuel_price=0):

        self.fuel_price = fuel_price
        self.heat_rate = heat_rate

        super().__init__(name=name, interest=interest, 
            year_num=year_num, capital_cost=capital_cost,
            F_O_and_M=F_O_and_M, V_O_and_M=V_O_and_M, 
            capacity=capacity, capacity_factor=capacity_factor)
        
        self.calc_efficiency()
        self.calc_LCOE()

    def calc_efficiency(self):
        """Calculate the efficiency with heat rate."""
        BTU_PER_KWH = 3412.1414799
        self.efficiency = BTU_PER_KWH / self.heat_rate 

    def calc_LCOE(self):
        """Calculate LCOE with source's properties including fuel."""

        HOURS_PER_YEAR = 8760
        KWH_PER_MWH = 1000
        BTU_PER_MMBTU = 1E6
        self.capital_term = ((self.capital_cost * self.CRF) 
                           / (HOURS_PER_YEAR * self.capacity_factor))
        self.fixed_term = (self.F_O_and_M 
                        / (HOURS_PER_YEAR * self.capacity_factor))
        self.variable_term = self.V_O_and_M / KWH_PER_MWH
        self.fuel_term = ((self.fuel_price / BTU_PER_MMBTU)
                         * self.heat_rate)
        self.LCOE_kWh = (self.capital_term + self.fixed_term 
                       + self.variable_term + self.fuel_term)
        self.LCOE = self.LCOE_kWh * KWH_PER_MWH

    def print_fuel_info(self):
        print('-' * 70)
        print(f"Fuel Information of '{self.name}'")
        print(f'Fuel costs: ${self.fuel_price}/mmBTU')
        print(f'Heat rate: {self.heat_rate} BTU/kwh')
        print(f'Fuel efficiency: {round(self.efficiency * 100, 2)}%')
        print('-' * 70)

    def print_cost_distribution_info(self, *, graph=False):
        print('-' * 70)
        print(f"Cost Distribution Information of '{self.name}' source")
        print(f'Capital term: '
            f'{round((self.capital_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Fixed term: '
            f'{round((self.fixed_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Variable term: '
            f'{round((self.variable_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Fuel term: '
            f'{round((self.fuel_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Total LCOE: ${round(self.LCOE, 2)}/MWh')
        print('-' * 70)

        if graph:
            labels = ('Capital', 'Fixed', 'Variable',
                       'Fuel')
            sizes = [self.capital_term, self.fixed_term,
                    self.variable_term, self.fuel_term]
            colors = ['orange', 'yellowgreen', 'lightcoral',
                    'lightskyblue']
            plt.pie(sizes, colors=colors, autopct='%1.1f%%',
                    pctdistance=1.15, startangle=140, normalize=True)
            plt.legend(labels, loc="best")
            plt.axis('equal')
            plt.show()