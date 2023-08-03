import unittest
from datetime import date
import sys
sys.path.append("./")
# import battery
from tires.octoprime import octoprimeTires
import random

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear_sensor = random.uniform(3.0,4.0)
        tires = octoprimeTires(tires_wear_sensor)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_wear_sensor = random.uniform(0.0,3.0)
        tires = octoprimeTires(tires_wear_sensor)
        self.assertFalse(tires.needs_service())

if __name__ == "__main__":
    unittest.main()