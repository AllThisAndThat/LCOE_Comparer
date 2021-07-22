"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: EnergySource.py (class)
Description: Stores class that handles the EnergySource class
"""
import matplotlib.pyplot as plt

class EnergySource:
    '''
    Describes and derives properties of energy sources from given properties
    
    Attributes:
    interest - the interest or discount rate as a percentage (unitless)
    i - the interest as a decimal (unitless)
    year_num and n - lifetime of powerplant (unitless)
    CRF - capital recovery factor (1/yr)
    capital_cost - initial cost for a given capacity ($/kW)
    F_O_and_M - fixed operation and maintaince cost that is constant ($/kW-yr)
    V_O_and_M - variable operation and maintaince cost ($/MWh)
    fuel_price - cost for fuel ($/mmBTU)
    heat_rate - measure of efficiency (BTU/kwh)
    capacity - maximum capacity of the power plant (MWh)
    capacity_factor - the ratio of actual power_production over capacity (unitless)
    LCOE- the levelized cost of energy ($/MWh)
    '''

    num_of_sources = 0
    INDUSTRY_I = 5

    def __init__(self, *, name, interest=INDUSTRY_I, year_num, capital_cost, F_O_and_M=0,
                 V_O_and_M=0, fuel_price=0, heat_rate=0, capacity, capacity_factor):
        self.name = name
        self.i = interest / 100
        self.n = year_num
        self.calc_CRF()

        self.capital_cost = capital_cost
        self.F_O_and_M = F_O_and_M
        self.V_O_and_M = V_O_and_M
        self.fuel_price = fuel_price
        self.heat_rate = heat_rate
        self.calc_efficiency()

        self.capacity = capacity
        self.capacity_factor = capacity_factor
        self.calc_LCOE()

        EnergySource.num_of_sources += 1

    def calc_CRF(self):
        '''
        Calculates the capital recovery factor based on interest and annuity

        '''
        self.CRF = (self.i*(1 + self.i)**self.n) / (((1 + self.i)**self.n) - 1)

    def calc_efficiency(self):
        '''
        Calculates the efficiency of an energy source that uses fuel based on heat rate
        
        '''
        BTU_PER_KWH = 3412.1414799
        if self.heat_rate:
            self.efficiency = BTU_PER_KWH / self.heat_rate
        else:
            self.efficiency = None 

    def calc_LCOE(self):
        '''
        Calculates the levelized cost of energy based on a variety of power plant costs
        
        '''
        HOURS_PER_YEAR = 8760
        KWH_PER_MWH = 1000
        BTU_PER_MMBTU = 1E6
        self.capital_term = (self.capital_cost * self.CRF) / (HOURS_PER_YEAR * self.capacity_factor)
        self.fixed_term = self.F_O_and_M / (HOURS_PER_YEAR * self.capacity_factor)
        self.variable_term = self.V_O_and_M / KWH_PER_MWH
        self.fuel_term = (self.fuel_price / BTU_PER_MMBTU) * self.heat_rate
        self.LCOE_kWh = self.capital_term + self.fixed_term + self.variable_term + self.fuel_term
        self.LCOE = self.LCOE_kWh * KWH_PER_MWH


    def print_info(self):
        print('-' * 70)
        print('General Information')
        print(f'Source: {self.name}')
        print(f'Capacity: {self.capacity} MW')
        print(f'Capacity Factor: {self.capacity_factor}')
        print(f'Used capital recovery factor: {round(self.CRF, 3)}')
        print(f'Levelized Cost ${round(self.LCOE, 2)}/MWh')
        print('-' * 70)

    def print_power_info(self):
        print('-' * 70)
        print('Power Information')
        print(f'Total capacity: {self.capacity} MW')
        print(f'Capacity factor: {self.capacity_factor}')
        print(f'Actual average power: {round(self.capacity * self.capacity_factor, 2)} MW')
        print('-' * 70)

    def print_fuel_info(self):
        print('-' * 70)
        print('Fuel Information')
        print(f'Fuel costs: ${self.fuel_price}/mmBTU')
        print(f'Heat rate: {self.heat_rate} BTU/kwh')
        print(f'Fuel efficiency: {round(self.efficiency * 100, 2)}%')
        print('-' * 70)

    def print_cost_distribution_info(self,*, graph=False):
        print('-' * 70)
        print('Cost Distribution Information')
        print(f'Capital term: {round((self.capital_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Fixed term: {round((self.fixed_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Variable term: {round((self.variable_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Fuel term: {round((self.fuel_term / self.LCOE_kWh) * 100, 2)}%')
        print(f'Total LCOE: ${round(self.LCOE, 2)}/MWh')
        print('-' * 70)

        if graph:
            labels = 'Capital Term', 'Fixed Term', 'Variable Term', 'Fuel Term'
            sizes = [self.capital_term, self.fixed_term, self.variable_term, self.fuel_term]
            colors = ['orange', 'yellowgreen', 'lightcoral', 'lightskyblue']
            plt.pie(sizes, colors=colors, autopct='%1.1f%%', pctdistance=1.15, startangle=140, normalize=True)
            plt.legend(labels, loc="best")
            plt.axis('equal')
            plt.show()
