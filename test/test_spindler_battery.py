import unittest
from datetime import date
from battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        # Test case where service is needed
        battery = SpindlerBattery(date(2022, 1, 1), date(2023, 6, 1))
        self.assertTrue(battery.needs_service())

        # Test case where service is not needed
        battery = SpindlerBattery(date(2023, 1, 1), date(2023, 6, 1))
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
