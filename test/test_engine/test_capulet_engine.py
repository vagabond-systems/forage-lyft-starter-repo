import unittest
from car_module.car_components.engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def check_needs_service_true_case(self):
        capulet = CapuletEngine(current_mileage=30001,last_service_mileage=0)
        self.assertTrue(capulet.needs_service())

    def check_needs_service_false_case(self):
        capulet = CapuletEngine(current_mileage=30000,last_service_mileage=0)
        self.assertFalse(capulet.needs_service())