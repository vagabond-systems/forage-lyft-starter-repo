import unittest
from datetime import datetime
from battery.nubinBattery import NubinBattery
from battery.spindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class NubbinBatteryTest(unittest.TestCase):
    def test_battery_should_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = NubinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class SpindlerBatteryTest(unittest.TestCase):
    def test_battery_should_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_served(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class CapuletEngineTest(unittest.TestCase):
    def test_engine_should_be_served(self):
        current_mileage = 50000
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_served(self):
        current_mileage = 20000
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class SternmanEngineTest(unittest.TestCase):
    def test_engine_should_be_served(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_served(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class WilloughbyEngineTest(unittest.TestCase):
    def test_engine_should_be_served(self):
        current_mileage = 80000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_served(self):
        current_mileage = 20000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
