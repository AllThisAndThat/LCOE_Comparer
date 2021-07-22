import unittest
from energy_source import EnergySource

class TestEnergySource(unittest.TestCase):
    
    def setUp(self):
        source1 = {
            'name': 'Coal',
            'interest': 10,
            'year_num': 20,
            'capital_cost': 3636,
            'F_O_and_M': 42.1,
            'V_O_and_M': 4.6,
            'fuel_price': 1.95,
            'heat_rate': 10000,
            'capacity': 650,
            'capacity_factor': 0.475
        }
        source2 = {
            'name': 'Natural Gas',
            'interest': 20,
            'year_num': 30,
            'capital_cost': 978,
            'F_O_and_M': 11,
            'V_O_and_M': 3.5,
            'fuel_price': 3.95,
            'heat_rate': 6600,
            'capacity': 702,
            'capacity_factor': 0.568    
        }
        self.plant1 = EnergySource(**source1)
        self.plant2 = EnergySource(**source2)

    def test_calc_CRF(self):
        self.assertEqual(round(self.plant1.CRF, 3), 0.117)
        self.assertEqual(round(self.plant2.CRF, 3), 0.201)

    def test_calc_efficiency(self):
        self.assertEqual(round(self.plant1.efficiency, 3), 0.341)
        self.assertEqual(round(self.plant2.efficiency, 3), 0.517)

    def test_calc_LCOE(self):
        self.assertEqual(round(self.plant1.LCOE, 2), 136.86)
        self.assertEqual(round(self.plant2.LCOE, 2), 71.26)

if __name__ == '__main__':
    unittest.main()