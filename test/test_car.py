import unittest
from datetime import datetime

from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_batteryShouldBeServiced(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        oldNubbin = NubbinBattery(last_service_date, self.today)
        self.assertTrue(oldNubbin.needs_service())

    def test_batteryShouldNotBeServiced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        newNubbin = NubbinBattery(last_service_date, self.today)
        self.assertFalse(newNubbin.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_batteryShouldBeServiced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        oldSpindler = SpindlerBattery(last_service_date, self.today)
        self.assertTrue(oldSpindler.needs_service())

    def test_batteryShouldNotBeServiced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        oldSpindler = SpindlerBattery(last_service_date, self.today)
        self.assertFalse(oldSpindler.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        self.last_service_mileage = 0

    def test_engineShouldBeServiced(self):
        current_mileage = 31000
        oldEngine = CapuletEngine(current_mileage, self.last_service_mileage)
        self.assertTrue(oldEngine.needs_service())

    def test_engineShouldNotBeServiced(self):
        current_mileage = 28000
        newEngine = CapuletEngine(current_mileage, self.last_service_mileage)
        self.assertFalse(newEngine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engineShouldBeServiced(self):
        warningLightIsOn = True
        oldEngine = SternmanEngine(warningLightIsOn)
        self.assertTrue(oldEngine.needs_service())

    def test_engineShouldNotBeServiced(self):
        warningLightIsOn = False
        newEngine = SternmanEngine(warningLightIsOn)
        self.assertFalse(newEngine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def setUp(self):
        self.last_service_mileage = 0

    def test_engineShouldBeServiced(self):
        current_mileage = 62000

        oldEngine = WilloughbyEngine(current_mileage, self.last_service_mileage)
        self.assertTrue(oldEngine.needs_service())

    def test_engineShouldNotBeServiced(self):
        current_mileage = 59999

        newEngine = WilloughbyEngine(current_mileage, self.last_service_mileage)
        self.assertFalse(newEngine.needs_service())


if __name__ == '__main__':
    unittest.main()
