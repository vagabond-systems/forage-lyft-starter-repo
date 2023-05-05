import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class TestCalliope(unittest.TestCase):
    def battery_needs_service(self):
        # Set up a Calliope instance with a last service date of January 1st, 2020,
        # a current mileage of 80000, and a last service mileage of 50000
        self.calliope = SpindlerBattery(last_service_date=datetime(2020, 1, 1))

        car = SpindlerBattery(datetime.now().date())
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.calliope = SpindlerBattery(last_service_date=datetime(2022, 4, 7))

        car = SpindlerBattery(datetime.now().date())
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        self.current_mileage = 80001
        self.last_service_mileage = 0
        service = self.current_mileage-self.last_service_mileage >= 30000

        car = CapuletEngine(service)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.current_mileage = 20001
        self.last_service_mileage = 0
        service = self.current_mileage-self.last_service_mileage >= 30000

        car = CapuletEngine(service)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        self.Glissade = SpindlerBattery(last_service_date=datetime(2008, 4, 6))

        car = SpindlerBattery(datetime.now().date())
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.Glissade = SpindlerBattery(last_service_date=datetime(2021, 4, 6))

        car = SpindlerBattery(datetime.now().date())
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        self.current_mileage = 60001
        self.last_service_mileage = 0
        service = self.current_mileage - self.last_service_mileage > 60000

        car = CapuletEngine(service)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.current_mileage = 60001
        self.last_service_mileage = 50000
        service = self.current_mileage - self.last_service_mileage > 60000

        car = CapuletEngine(service)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        self.palindrome = SpindlerBattery(last_service_date=datetime(2008, 4, 6))

        car = SpindlerBattery(datetime.now().date())
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.Glissade = SpindlerBattery(last_service_date=datetime(2021, 4, 6))

        car = SpindlerBattery(datetime.now().date())
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        
        warning_light_is_on = True

        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        
        warning_light_is_on = False

        car = SternmanEngine(warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        
        self.rorschach = NubbinBattery(last_service_date=datetime(2022, 7, 8))
        
        car = NubbinBattery(last_service_date=datetime.now().date)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        
        self.rorschach = NubbinBattery(last_service_date=datetime(2022, 7, 8))
        

        car = NubbinBattery(self.rorschach(datetime.now().date()))
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        
        current_mileage = 60001
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage-last_service_mileage >= 60000)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage-last_service_mileage >= 60000)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        
        self.rorschach = NubbinBattery(last_service_mileage=datetime(2013, 6, 9))

        car = NubbinBattery(last_service_date=datetime.now().date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.rorschach = NubbinBattery(last_service_mileage=datetime(2013, 6, 9))
     

        car = NubbinBattery(last_service_date=datetime.now().date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        
        current_mileage = 40001
        last_service_mileage = 0

        car = CapuletEngine( current_mileage-last_service_mileage >= 30000)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        
        current_mileage = 10000
        last_service_mileage = 0

        car = CapuletEngine(current_mileage-last_service_mileage >= 30000)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
