import unittest
from datetime import datetime
import sys
sys.path.append("./")
# from engine.model.calliope import Calliope
# from engine.model.glissade import Glissade
# from engine.model.palindrome import Palindrome
# from engine.model.rorschach import Rorschach
# from engine.model.thovex import Thovex
# from car import Engine,Battery
# from battery.Nubbin import NubbinBattery
# from battery.spindler import SpindlerBattery
# from battery.battery import Battery
from car_factory import CarFactory
from serviceable import Serviceable
from car import Car
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        
        car = CarFactory().create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service(car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory().create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory().create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service(car))


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service(car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory().create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory().create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(Car.needs_service(car))


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory().create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(Car.needs_service(car))

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = CarFactory().create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(Car.needs_service(car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory().create_palindrome(last_service_date, last_service_date, warning_light_is_on)
        self.assertTrue(Car.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory().create_palindrome(last_service_date, last_service_date, warning_light_is_on)
        self.assertFalse(Car.needs_service(car))


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_rorschach(today, last_service_date, current_mileage,last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_rorschach(today, last_service_date, current_mileage,last_service_mileage)
        self.assertFalse(Car.needs_service(car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory().create_rorschach(last_service_date, last_service_date, current_mileage,last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory().create_rorschach(last_service_date, last_service_date, current_mileage,last_service_mileage)
        self.assertFalse(Car.needs_service(car))


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_thovex(today, last_service_date, current_mileage,last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_thovex(today, last_service_date, current_mileage,last_service_mileage)
        self.assertFalse(Car.needs_service(car))

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory().create_thovex(last_service_date, last_service_date, current_mileage,last_service_mileage)
        self.assertTrue(Car.needs_service(car))

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory().create_thovex(last_service_date, last_service_date, current_mileage,last_service_mileage)
        self.assertFalse(Car.needs_service(car))


if __name__ == '__main__':
    unittest.main()
