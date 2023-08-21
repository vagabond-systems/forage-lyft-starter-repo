import unittest
from car_module.car_components.battery import NubbinBattery
from datetime import date

class TestNubbinBattery(unittest.TestCase):
    def check_needs_service_true_case(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-5)
        nubbin = NubbinBattery(current_date,last_service_date)
        self.assertTrue(nubbin.needs_service())

    def check_needs_service_flase_case(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-1)
        nubbin = NubbinBattery(current_date,last_service_date)
        self.assertFalse(nubbin.needs_service())
