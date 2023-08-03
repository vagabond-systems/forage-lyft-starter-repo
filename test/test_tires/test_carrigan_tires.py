import unittest
from datetime import date
import sys
sys.path.append("./")
# import battery
from tires.carrigan import carriganTires
import random

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        sesnsor_list=[]
        for t in range(4):
            tires_wear_sensor = random.uniform(0.9,1.0)
            sesnsor_list.append(tires_wear_sensor)
        tires = carriganTires(sesnsor_list)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sesnsor_list=[]
        for t in range(4):
            tires_wear_sensor = random.uniform(0.0,0.9)
            sesnsor_list.append(tires_wear_sensor)
        tires = carriganTires(sesnsor_list)
        self.assertFalse(tires.needs_service())

if __name__ == "__main__":
    unittest.main()