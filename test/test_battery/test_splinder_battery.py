import unittest
from datetime import date, timedelta
from battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = date.today() - timedelta(days=730)

        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        last_service_date = date.today() - timedelta(days=365)

        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())