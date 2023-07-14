import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery

class NubbinBatteryTest(unittest.TestCase):
    def test_battery_should_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date,today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = NubbinBattery(last_service_date,today)
        self.assertFalse(battery.needs_service())   




if __name__ == '__main__':
    unittest.main()