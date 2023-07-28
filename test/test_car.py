import unittest
from datetime import date, timedelta
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 0
        current_mileage = 30005

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 20000

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 0
        current_mileage = 60005

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 60000

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        warning_light_on = False

        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = date.today() - timedelta(days=730)

        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        last_service_date = date.today() - timedelta(days=365)

        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = date.today() - timedelta(days=1460)

        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        last_service_date = date.today() - timedelta(days=730)

        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
