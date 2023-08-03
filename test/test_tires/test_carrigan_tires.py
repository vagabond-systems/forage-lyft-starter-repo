import unittest
from datetime import date
import sys
sys.path.append("./")
# import battery
from tires.carrigan import carriganTires
import random

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear_sensor = random.uniform(0.9,4.0)
        tires = carriganTires(tires_wear_sensor)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_wear_sensor = random.uniform(0.0,0.9)
        tires = carriganTires(tires_wear_sensor)
        self.assertFalse(tires.needs_service())

if __name__ == "__main__":
    unittest.main()