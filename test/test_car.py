import unittest
from datetime import date

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery


class TestCalliope(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30002
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29999
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = date(2022, 12, 4).isoformat()
        last_service_date = date(2019, 12, 4).isoformat()

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
      
        current_date = 0
        last_service_date = 0

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())


class TestGlissade(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60002
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = date(2022, 12, 4).isoformat()
        last_service_date = date(2019, 12, 4).isoformat()

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
      
        current_date = 0
        last_service_date = 0

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = date(2022, 12, 4).isoformat()
        last_service_date = date(2019, 12, 4).isoformat()

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
      
        current_date = 0
        last_service_date = 0

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())

class TestRorschach(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60002
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = date(2022, 12, 4).isoformat()
        last_service_date = date(2019, 12, 4).isoformat()

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
      
        current_date = 0
        last_service_date = 0

        nubbin = NubbinBattery(last_service_date, current_date)
        self.assertFalse(nubbin.needs_service())

class TestThovex(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30002
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29999
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = date(2022, 12, 4).isoformat()
        last_service_date = date(2019, 12, 4).isoformat()
        
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
      
        current_date = 0
        last_service_date = 0

        nubbin = NubbinBattery(last_service_date, current_date)
        self.assertFalse(nubbin.needs_service())