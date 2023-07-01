import unittest
from Tire.Octoprime_tire import OctoprimeTire

class TestOctoprime(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        value_of_worn_in_tire=[0.9, 0.1, 0.2, 0.1]

        TIRE = OctoprimeTire(value_of_worn_in_tire)
        self.assertTrue(TIRE.needs_service())

    def test_battery_should_NOT_be_serviced(self):
        value_of_worn_in_tire = [0.2, 0.1, 0.2, 0.1]

        TIRE = OctoprimeTire(value_of_worn_in_tire)
        self.assertTrue(TIRE.needs_service())

