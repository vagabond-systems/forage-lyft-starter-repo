import unittest
from car_module.car_components.battery import SpindlerBattery
from datetime import date

class TestSpindlerBattery(unittest.TestCase):
    def check_needs_service_true_case(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-4)
        nubbin = SpindlerBattery(current_date,last_service_date)
        self.assertTrue(nubbin.needs_service())

    def check_needs_service_flase_case(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-1)
        nubbin = SpindlerBattery(current_date,last_service_date)
        self.assertFalse(nubbin.needs_service())
