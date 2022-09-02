import unittest
from datetime import datetime
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery


class test_SpindlerBattery(unittest.TestCase):
    def test_SpindlerBattery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_SpindlerBattery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year + 1)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

class test_NubbinBattery(unittest.TestCase):
    def test_NubbinBattery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_NubbinBattery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
