import unittest
from car_module.car_components.engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def check_needs_service_true_case(self):
        capulet = WilloughbyEngine(current_mileage=60001,last_service_mileage=0)
        self.assertTrue(capulet.needs_service())

    def check_needs_service_false_case(self):
        capulet = WilloughbyEngine(current_mileage=60000,last_service_mileage=0)
        self.assertFalse(capulet.needs_service())