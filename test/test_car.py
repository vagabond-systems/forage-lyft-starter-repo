import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car_factory import CarFactory

class Test_Calliope(unittest.TestCase):
    def test_needs_servicing(self):
        car = CarFactory.create_calliope(datetime.today().date(), datetime.today().date(), 35000, 0)
        self.assertTrue(car.needs_service())

    def test_does_not_need_servicing(self):
        car = CarFactory.create_calliope(datetime.today().date(), datetime.today().date(), 300, 0)
        self.assertFalse(car.needs_service())

class Test_Glissade(unittest.TestCase):
    def test_needs_servicing(self):
        car = CarFactory.create_glissade(datetime.today().date(), datetime.today().date(), 65000, 0)
        self.assertTrue(car.needs_service())

    def test_does_not_need_servicing(self):
        car = CarFactory.create_glissade(datetime.today().date(), datetime.today().date(), 300, 0)
        self.assertFalse(car.needs_service())

class Test_Palindrome(unittest.TestCase):
    def test_needs_servicing(self):
        car = CarFactory.create_palindrome(datetime.today().date(), datetime.today().date(), True)
        self.assertTrue(car.needs_service())

    def test_does_not_need_servicing(self):
        car = CarFactory.create_palindrome(datetime.today().date(), datetime.today().date(), False)
        self.assertFalse(car.needs_service())


class Test_Rorschach(unittest.TestCase):
    def test_needs_servicing(self):
        car = CarFactory.create_rorschach(datetime.today().date(), datetime.today().date(), 65000, 0)
        self.assertTrue(car.needs_service())

    def test_does_not_need_servicing(self):
        car = CarFactory.create_rorschach(datetime.today().date(), datetime.today().date(), 300, 0)
        self.assertFalse(car.needs_service())

class Test_Thovex(unittest.TestCase):
    def test_needs_servicing(self):
        car = CarFactory.create_thovex(datetime.today().date(), datetime.today().date(), 35000, 0)
        self.assertTrue(car.needs_service())

    def test_does_not_need_servicing(self):
        car = CarFactory.create_thovex(datetime.today().date(), datetime.today().date(), 300, 0)
        self.assertFalse(car.needs_service())
