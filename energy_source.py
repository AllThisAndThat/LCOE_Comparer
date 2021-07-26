"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: energy_source.py (class)
Content: EnergySource
Description: Store class to handle energy source properties
"""

import matplotlib.pyplot as plt

class EnergySource:
    """
    Derive properties of energy sources from given properties.
    
    Attributes:
    interest - the interest or discount rate as a percentage
    i - the interest as a decimal
    year_num and n - lifetime of powerplant
    CRF - capital recovery factor (1/yr)
    capital_cost - initial cost for a given capacity ($/kW)
    f_o_and_m - fixed operation and maintaince cost ($/kW-yr)
    v_o_and_m - variable operation and maintaince cost ($/MWh)
    capacity - maximum capacity of the power plant (MWh)
    capacity_factor - actual / capacity (unitless)
    LCOE - the levelized cost of energy ($/MWh)
    num_of_sources - recond of instances
    fuel_cost - cost of fuel for source ($/mmBTU)
    heat_rate - measure of efficiency (BTU/kWh)
    """
    num_of_sources = 0
    Industry_I = 5
    Industry_N = 20

    def __init__(self, *, name='No Name', capacity=None, 
        capacity_factor=None, interest=Industry_I, 
        year_num=Industry_N, capital_cost=None, f_o_and_m=None,
        v_o_and_m=None, fuel_cost=None, heat_rate=None):
        """Set variables and derive properties."""
        self.name = name
        
        self.capacity = capacity
        self.capacity_factor = capacity_factor

        self.i = interest / 100
        self.n = year_num

        self.capital_cost = capital_cost
        self.f_o_and_m = f_o_and_m
        self.v_o_and_m = v_o_and_m

        self.fuel_cost = fuel_cost
        self.heat_rate = heat_rate

        self.calc_CRF()
        self.calc_LCOE()

        EnergySource.num_of_sources += 1

    def calc_CRF(self):
        """Calculate the CRF based on interest and annuity."""
        self.CRF = ((self.i * (1 + self.i)**self.n) 
            / (((1 + self.i)**self.n) - 1))

    def calc_LCOE(self):
        """
        Calculate LCOE based on variety of costs.
        
        capital_term - capital cost after conversion ($/kWh)
        fixed_term - fixed O&M after conversion ($/kWh)
        variable_term - variable O&M after conversion ($/kWh)
        fuel_term - fuel cost after conversion ($/kWh)

        LCOE_kWh ($/kWh) and LCOE ($/MWh)
        """
        HOURS_PER_YEAR = 8760
        KWH_PER_MWH = 1000
        MMBTU_PER_BTU = 1e6

        if self.capital_cost == None:
            self.capital_term = 0
        elif self.CRF == None:
            self.capital_term = 0
        elif self.capacity_factor == None:
            self.capital_term = 0
        else:
            self.capital_term = ((self.capital_cost * self.CRF) 
                / (HOURS_PER_YEAR * self.capacity_factor))
    
        if self.f_o_and_m == None:
            self.fixed_term = 0
        elif self.capacity_factor == None:
            self.fixed_term = 0
        else:
            self.fixed_term = (self.f_o_and_m 
                / (HOURS_PER_YEAR * self.capacity_factor))

        if self.v_o_and_m == None:
            self.variable_term = 0
        else:
            self.variable_term = self.v_o_and_m / KWH_PER_MWH

        if self.fuel_cost == None:
            self.fuel_term = 0
        elif self.heat_rate == None:
            self.fuel_term = 0
        else:
            self.fuel_term = (self.fuel_cost / MMBTU_PER_BTU
            * self.heat_rate)

        self.LCOE_kWh = (self.capital_term 
            + self.fixed_term 
            + self.variable_term
            + self.fuel_term)
        self.LCOE = self.LCOE_kWh * KWH_PER_MWH

    def print_info(self):
        """Print general information of source."""
        print('-' * 70)
        print(f"General Information of '{self.name}' source")
        print(f"Capacity: {self.capacity} MW")
        print(f"Used capital recovery factor: {round(self.CRF, 3)}")
        print(f"Levelized Cost ${round(self.LCOE, 2)}/MWh")
        print('-' * 70)

    def print_power_info(self):
        """Print power properties of source."""
        print('-' * 70)
        print(f"Power Information of '{self.name}' source")
        print(f"Total capacity: {self.capacity} MW")
        print(f"Capacity factor: {self.capacity_factor}")
        print(f"Actual average power: "
            f"{round(self.capacity * self.capacity_factor, 2)} MW")
        print('-' * 70)

    def print_cost_distribution_info(self, *, graph=False):
        """Present different costs of a source. Graph as option."""
        print('-' * 70)
        print(f"Cost Distribution Information of "
            f"'{self.name}' source")
        try:
            print(f"Capital: "
                f"{round((self.capital_term / self.LCOE_kWh) * 100, 2)}%")
            print(f"Fixed: "
                f"{round((self.fixed_term / self.LCOE_kWh) * 100, 2)}%")
            print(f"Variable: "
                f"{round((self.variable_term / self.LCOE_kWh) * 100, 2)}%")
            print(f"Fuel: "
                f"{round((self.fuel_term / self.LCOE_kWh) * 100, 2)}%")
        except ZeroDivisionError:
            if graph: print("No Data to Graph")
        print(f"Total LCOE: ${round(self.LCOE, 2)}/MWh")
        print('-' * 70)

        if graph and self.LCOE:
            labels = []
            sizes = []
            if self.capital_term:
                labels.append('Capital')
                sizes.append(self.capital_term)
            if self.fixed_term:
                labels.append('Fixed')
                sizes.append(self.fixed_term)
            if self.variable_term:
                labels.append('Variable')
                sizes.append(self.variable_term)
            if self.fuel_term:
                labels.append('Fuel')
                sizes.append(self.fuel_term)
            colors = ['orange', 'yellowgreen', 'lightcoral',
                'lightblue']
            plt.pie(sizes, colors=colors, autopct='%1.1f%%',
                pctdistance=1.15, startangle=140, normalize=True)
            plt.legend(labels, loc="best")
            plt.axis('equal')
            plt.show()

    def print_fuel_info(self):
        """Print fuel properties of source."""
        print('-' * 70)
        print(f"Fuel Information of '{self.name}' source")
        if self.fuel_cost:
            print(f"Fuel Cost: ${self.fuel_cost}/mmBTU")
        if self.heat_rate:
            print(f"Heat Rate: {self.heat_rate} BTU/kWh")
        if not self.fuel_cost or not self.heat_rate:
            print("This source doesn't have fuel information.")
        print('-' * 70)

    def print_efficiency_info(self):
        """Print efficiency properties of source."""
        BTU_PER_KWH = 3412.14148

        print('-' * 70)
        print(f"Efficiency Information of '{self.name}' source")
        if self.heat_rate:
            print(f"Heat Rate: {self.heat_rate} BTU/kWh")
            print(f"Efficiency: "
                f"{round((BTU_PER_KWH / self.heat_rate) * 100, 2)}%")
        else:
            print("This source doesn't have efficiency information.")
        print('-' * 70)