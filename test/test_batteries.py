import unittest
from datetime import date, datetime, timedelta
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        # A Spindler battery must be serviced every 2 years.
        today = datetime.today().date()
        more_than_three_years_ago = today - timedelta(days=365*3+1)  # 1096 days ago
        less_than_three_years_ago = today - timedelta(days=365*3-1)  # 1094 days ago
        self.spindler_that_needs_service = SpindlerBattery(
            current_date=today,
            last_service_date=more_than_three_years_ago
        )
        self.spindler_that_doesnt_need_service = SpindlerBattery(
            current_date=today,
            last_service_date=less_than_three_years_ago
        )

    def test_should_need_service(self):
        self.assertTrue(
            self.spindler_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.spindler_that_doesnt_need_service.needs_service()
        )


class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        # A Nubbin battery must be serviced every 4 years.
        today = datetime.today().date()
        more_than_four_years_ago = today - timedelta(days=365*4+1)  # 1461 days ago
        less_than_four_years_ago = today - timedelta(days=365*4-1)  # 1459 days ago
        self.nubbin_that_needs_service = NubbinBattery(
            current_date=today,
            last_service_date=more_than_four_years_ago
        )
        self.nubbin_that_doesnt_need_service = NubbinBattery(
            current_date=today,
            last_service_date=less_than_four_years_ago
        )

    def test_should_need_service(self):
        self.assertTrue(
            self.nubbin_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.nubbin_that_doesnt_need_service.needs_service()
        )

if __name__ == "__main__":
    unittest.main()