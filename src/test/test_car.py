import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.splindler_battery import SplindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine_capulet = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        self.assertTrue(engine_capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine_capulet = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        self.assertFalse(engine_capulet.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine_willoughby = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        self.assertTrue(engine_willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine_willoughby = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        self.assertFalse(engine_willoughby.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine_sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine_sternman.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine_sternman = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine_sternman.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())


class TestSplindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SplindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SplindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensors = [0.1, 0.2, 0.4, 0.9]

        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0.1, 0.2, 0.4, 0.5]

        tire = CarriganTire(sensors)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensors = [1, 1, 1, 1]

        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0.8, 0.6, 0.7, 0.8]

        tire = OctoprimeTire(sensors)
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
