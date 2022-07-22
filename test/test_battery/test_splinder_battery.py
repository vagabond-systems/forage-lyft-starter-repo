import unittest

from battery.SplinderBattery import SplinderBattery
from datetime import date

class TestSplinderBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2021-06-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
    

