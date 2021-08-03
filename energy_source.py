"""
Author: Lucas Hudson
Summer 2021
Project Name: Demand 2050
File: energy_source.py (class)
Content: EnergySource
Description: Store class to handle energy source properties
"""

import sys
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
    co2_rate - measure of Co2 max per energy produced (kg-Co2/mmBTU)
    co2_tax - cost per mass of Co2 produced from source ($/kg-Co2)
    land_rate - measure of power density of land (W/m^2)
    land_tax - cost per unit area of land ($/m^2)
    subsidy - external value for type of source ($/kWh)
    """
    instances = []
    # Industry variables
    industry_i = 5
    industry_n = 20
    co2_tax = 0
    land_tax = 0
    # Time conversions
    HOURS_PER_YEAR = 8760
    # Energy conversions
    BTU_PER_KWH = 3412.14148
    HOURS_PER_YEAR = 8760
    KWH_PER_MWH = 1000
    MMBTU_PER_BTU = 1e6
    KWH_PER_MMBTU = 293.07107
    # Power conversions
    KW_PER_W = 1e-3

    def __init__(self, *, name='No Name', capacity=None, 
        capacity_factor=None, capital_cost=None, f_o_and_m=None,
        v_o_and_m=None, fuel_cost=None, heat_rate=None, 
        co2_rate=None, land_rate=None, subsidy=None):
        """Set and check variables and derive properties."""
        try:
            if type(name) != str:
                self.name = str(name)
                raise ValueError("Please enter a string "
                "for the name.")
            self.name = name

            if (capacity is not None) and (capacity < 0):
                raise ValueError("Capacity must be a "
                "non-negative number.")
            self.capacity = capacity
            if ((capacity_factor is not None)  
                and not (0 < capacity_factor < 1)):
                raise ValueError("Capacity_factor must be "
                "between 0 and 1.")
            self.capacity_factor = capacity_factor

            self.i = EnergySource.industry_i / 100
            self.n = EnergySource.industry_n

            self.capital_cost = capital_cost
            self.f_o_and_m = f_o_and_m
            self.v_o_and_m = v_o_and_m

            self.fuel_cost = fuel_cost
            if ((heat_rate is not None) 
                and (heat_rate < EnergySource.BTU_PER_KWH)):
                raise ValueError(f"heat_rate must exceed "
                f"{EnergySource.BTU_PER_KWH} BTU/KWH "
                f"(perfect efficiency).")
            self.heat_rate = heat_rate

            if (co2_rate is not None) and (co2_rate < 0):
                raise ValueError("co2_rate must be a "
                "non-negative number.")
            self.co2_rate = co2_rate

            if (land_rate is not None) and (land_rate <= 0):
                raise ValueError("land_rate must be a "
                "positive number.")
            self.land_rate = land_rate

            if (subsidy is not None) and (subsidy < 0):
                raise ValueError("subsidy must be a "
                "non-negative number.")
            self.subsidy = subsidy

            self.calc_CRF()
            self.calc_LCOE()
            self.calc_efficiency()

            EnergySource.instances.append(self)

        except ValueError as err:
            print('-' * 70)
            print("ERROR:")
            print(f"Instance Name: {self.name}")
            print(err)
            sys.exit()

    def calc_CRF(self):
        """Calculate the CRF based on interest and annuity."""
        self.CRF = ((self.i * (1 + self.i)**self.n) 
            / (((1 + self.i)**self.n) - 1))

    def calc_efficiency(self):
        """Calculate Efficiency for a source."""
        if self.heat_rate == None:
            self.efficiency = 0
        else:
            self.efficiency = (EnergySource.BTU_PER_KWH 
                / self.heat_rate)

    def calc_LCOE(self):
        """
        Calculate LCOE based on variety of costs.
        
        capital_term - capital cost after conversion ($/kWh)
        fixed_term - fixed O&M after conversion ($/kWh)
        variable_term - variable O&M after conversion ($/kWh)
        fuel_term - fuel cost after conversion ($/kWh)
        co2_tax_term - co2 tax after conversion ($/kWh)
        land_tax_term - land tax after conversion ($/kWh)
        subsidy_term - external subsidy for source ($/kWh)

        LCOE_kWh ($/kWh) and LCOE ($/MWh)
        """
        if self.capital_cost == None:
            self.capital_term = 0
        elif self.CRF == None:
            self.capital_term = 0
        elif self.capacity_factor == None:
            self.capital_term = 0
        else:
            
            self.capital_term = ((self.capital_cost * self.CRF) 
                / (EnergySource.HOURS_PER_YEAR 
                * self.capacity_factor))
    
        if self.f_o_and_m == None:
            self.fixed_term = 0
        elif self.capacity_factor == None:
            self.fixed_term = 0
        else:
            self.fixed_term = (self.f_o_and_m 
                / (EnergySource.HOURS_PER_YEAR 
                * self.capacity_factor))

        if self.v_o_and_m == None:
            self.variable_term = 0
        else:
            self.variable_term = (self.v_o_and_m 
                / EnergySource.KWH_PER_MWH)

        if self.fuel_cost == None:
            self.fuel_term = 0
        elif self.heat_rate == None:
            self.fuel_term = 0
        else:
            self.fuel_term = (self.fuel_cost 
            / EnergySource.MMBTU_PER_BTU * self.heat_rate)

        if self.co2_rate == None:
            self.co2_tax_term = 0;
        else:
            self.co2_tax_term = ((EnergySource.co2_tax * self.co2_rate) 
                / EnergySource.KWH_PER_MMBTU)
        
        if self.land_rate == None:
            self.land_tax_term = 0
        else:
            self.land_tax_term = ((EnergySource.land_tax * self.CRF) 
                / (EnergySource.HOURS_PER_YEAR 
                * (self.land_rate * EnergySource.KW_PER_W)))
        
        if self.subsidy == None:
            self.subsidy_term = 0
        else:
            self.subsidy_term = -self.subsidy

        self.LCOE_kWh = (self.capital_term 
            + self.fixed_term 
            + self.variable_term
            + self.fuel_term
            + self.co2_tax_term
            + self.land_tax_term
            + self.subsidy_term)
        self.LCOE = self.LCOE_kWh * EnergySource.KWH_PER_MWH

    def print_all(self):
        """Print all print methods for a source."""
        self.print_info()
        self.print_power_info()
        self.print_cost_distribution_info()
        self.print_fuel_info()
        self.print_efficiency_info()

    def print_cost_distribution_info(self, *, graph=False):
        """Present different costs of a source. Graph as option."""
        print('-' * 70)
        print(f"Cost distribution information of "
            f"'{self.name}' source:")
        term_names = ['Capital', 'Fixed', 'Variable', 'Fuel',
            'Co2 Tax', 'Land Tax', 'Subsidy']
        terms = [self.capital_term, self.fixed_term,
            self.variable_term, self.fuel_term,
            self.co2_tax_term ,self.land_tax_term, self.subsidy_term]
        try:
            for term_name, term in zip(term_names, terms):
                print(f"{term_name}: |"
                    f" ${round(term * 1e3, 2)}/MWh |"
                    f" {round((term / self.LCOE_kWh) * 100, 2)}%")
        except ZeroDivisionError:
            if graph: print("No Data to Graph")
        print(f"Total LCOE: ${round(self.LCOE, 2)}/MWh")
        print('-' * 70)

        if graph and self.LCOE:
            labels = []
            sizes = []
            for term_name, term in zip(term_names, terms):
                if (term) and (term > 0):
                    labels.append(term_name)
                    sizes.append(term)
            
            colors = ['orange', 'yellowgreen', 'lightcoral',
                'lightblue', 'firebrick', 'lightslategrey']
            plt.pie(sizes, colors=colors, autopct='%1.1f%%',
                pctdistance=1.15, startangle=140, normalize=True)
            plt.legend(labels, loc="best")
            plt.axis('equal')
            plt.show()

    def print_efficiency_info(self):
        """Print efficiency properties of source."""
        print('-' * 70)
        print(f"Efficiency information of '{self.name}' source:")
        if self.heat_rate == None:
            print("This source doesn't have efficiency information.")  
        else:
            print(f"Heat Rate: {self.heat_rate} BTU/kWh")
            print(f"Efficiency: "
                f"{round(self.efficiency * 100, 2)}%")
        print('-' * 70)

    def print_fuel_info(self):
        """Print fuel properties of source."""
        print('-' * 70)
        print(f"Fuel information of '{self.name}' source:")
        if self.fuel_cost:
            print(f"Fuel Cost: ${self.fuel_cost}/mmBTU")
        if self.heat_rate:
            print(f"Heat Rate: {self.heat_rate} BTU/kWh")
        if self.co2_rate:
            print(f"Co2 Rate: {self.co2_rate} kg-Co2/mmBTU")
        temp_list = [self.fuel_cost, self.heat_rate, self. co2_rate]
        if temp_list.count(None) == len(temp_list):
            print("This source doesn't have fuel information.")
        print('-' * 70)

    def print_info(self):
        """Print general information of source."""
        print('-' * 70)
        print(f"General information of '{self.name}' source:")
        if self.capacity != None:
            print(f"Capacity: {self.capacity} MW")
        if self.co2_rate != None:
            print(f"Co2 Rate: {self.co2_rate} Co2-kg/mmBTU")
        if self.land_rate != None:
            print(f"Land Rate: {self.land_rate} W/m^2")
        if self.subsidy != None:
            print(f"Subsidy: ${self.subsidy}/kwh")
        print(f"Used capital recovery factor: {round(self.CRF, 3)}")
        print(f"Levelized Cost ${round(self.LCOE, 2)}/MWh")
        print('-' * 70)

    def print_input_properties(self):
        """Print all input properties."""
        print('-' * 70)
        print(f"Input property information of '{self.name}' source:")
        print(f"Name: {self.name}")
        if self.capacity == None:
            print(f"Capacity: {self.capacity}")
        else:
            print(f"Capacity: {self.capacity} MWh")
        print(f"Capacity Factor: {self.capacity_factor}")
        print(f"Interest: {self.i * 100} %")
        print(f"Source Life: {self.n} years")
        if self.capital_cost == None:
            print(f"Capital Cost: {self.capital_cost}")
        else:
            print(f"Capital Cost: ${self.capital_cost}/kWh")
        if self.f_o_and_m == None:
            print(f"Fixed O&M: {self.f_o_and_m}")
        else:
            print(f"Fixed O&M: ${self.f_o_and_m}/kWh-yr")
        if self.v_o_and_m == None:
            print(f"Variable O&M: {self.v_o_and_m}")
        else:
            print(f"Variable O&M: ${self.v_o_and_m}/MWh")
        if self.fuel_cost == None:
            print(f"Fuel Cost: {self.fuel_cost}")
        else:
            print(f"Fuel Cost: ${self.fuel_cost}/mmBTU")
        if self.heat_rate == None:
            print(f"Heat Rate: {self.heat_rate}")
        else:
            print(f"Heat Rate: {self.heat_rate} BTU/kWh")
        if self.co2_rate == None:
            print(f"Co2 Rate: {self.co2_rate}")
        else:
            print(f"Co2 Rate: {self.co2_rate} kg-Co2/mmBTU")
        if self.co2_tax == None:
            print(f"Co2 Tax: {self.co2_tax}")
        else:
            print(f"Co2 Tax: ${self.co2_tax}/kg-Co2")
        if self.land_rate == None:
            print(f"Land Rate: {self.land_rate}")
        else:
            print(f"Land Rate: {self.land_rate} W/m^2")
        if self.land_tax == None:
            print(f"Land Tax: {self.land_tax}")
        else:
            print(f"Land Tax: ${self.land_tax}/m^2")
        if self.subsidy == None:
            print(f"Subsidy: {self.subsidy}")
        else:
            print(f"Subsidy: ${self.subsidy}/kWh")
        print('-' * 70)

    def print_power_info(self):
        """Print power properties of source."""
        print('-' * 70)
        print(f"Power information of '{self.name}' source:")
        if self.capacity != None:
            print(f"Total capacity: {self.capacity} MW")
        if self.capacity_factor != None:
            print(f"Capacity factor: {self.capacity_factor}")
        if self.capacity != None and self.capacity_factor != None:
            print(f"Actual average power: "
                f"{round(self.capacity * self.capacity_factor, 2)} MW")
        else:
            print("This source doesn't have power information.")
        print('-' * 70)

    @classmethod
    def print_all_instances(cls):
        """Print all instances of EnergySource class."""
        print('-' * 70)
        print("All energy sources:")
        for (count, instance) in enumerate(cls.instances, 1):
            print(f"{count}: {instance.name}")
        print('-' * 70)

    @classmethod
    def print_LCOE_comparison(cls):
        """Print LCOEs for all instances in order."""
        print('-' * 70)
        print("LCOE for all sources:")
        LCOES = {}
        for instance in cls.instances:
            LCOES[instance.LCOE] = instance.name
        for value, key in sorted(LCOES.items()):
            print(f"{key}: ${round(value, 2)}/MWh")
        print('-' * 70)
    
    @classmethod
    def set_co2_tax(cls, new_tax):
        """Set the co2 tax rate for the industry."""
        try:
            if new_tax < 0:
                raise ValueError("Co2 tax should be a "
                    "non-negative number.")
            cls.co2_tax = new_tax
        except ValueError as err:
            print(err)
            sys.exit()

    @classmethod
    def set_industry(cls, *, interest, loan_period,
        co2_tax = 0, land_tax = 0):
        """Set industry variables."""
        cls.set_industry_i(interest)
        cls.set_industry_n(loan_period)
        cls.set_co2_tax(co2_tax)
        cls.set_land_tax(land_tax)

    @classmethod
    def set_industry_i(cls, new_i):
        """set the interest for the industry"""
        try:
            if (new_i <= 0):
                    raise ValueError("Interest must be a "
                    "positive number.")
            cls.industry_i = new_i
        except ValueError as err:
            print(err)
            sys.exit()

    @classmethod
    def set_industry_n(cls, new_n):
        """set the loan period for the industry."""
        try:
            if (new_n <= 0):
                    raise ValueError("Loan period must be a "
                    "positive number.")
            cls.industry_n = new_n
        except ValueError as err:
            print(err)
            sys.exit()

    @classmethod
    def set_land_tax(cls, new_tax):
        """Set the land tax rate for the industry."""
        try:
            if new_tax < 0:
                raise ValueError("Land tax should be a "
                    "non-negative number.")
            cls.land_tax = new_tax
        except ValueError as err:
            print(err)
            sys.exit()
