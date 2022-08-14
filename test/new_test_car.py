import unittest
import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin import Nubbin
from battery.spindler import Spindler


class TestCalliope(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30002
        last_service_mileage = 1

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 20
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)

        spindler = Spindler(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)

        spindler = Spindler(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())

class TestGlissade(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 89043
        last_service_mileage = 20300
        
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 90
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date - 3)
        
        spindler = Spindler(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 2)
        
        spindler = Spindler(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())

class testPalindrome(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_indicator = True
        
        sternman = SternmanEngine(warning_indicator)
        self.assertTrue(sternman.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        warning_indicator = False
        
        sternman = SternmanEngine(warning_indicator)
        self.assertFalse(sternman.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        
        spindler = Spindler(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        
        spindler = Spindler(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())
        
class TestRorschach(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 89043
        last_service_mileage = 20300
        
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 90
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date - 5)
        
        nubbin = Nubbin(last_service_date, current_date)
        self.assertTrue(nubbin.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        
        nubbin = Nubbin(last_service_date, current_date)
        self.assertFalse(nubbin.needs_service())
        
class TestThovex(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30002
        last_service_mileage = 1

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 20
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date - 5)
        
        nubbin = Nubbin(last_service_date, current_date)
        self.assertTrue(nubbin.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        
        nubbin = Nubbin(last_service_date, current_date)
        self.assertFalse(nubbin.needs_service())
        
        

        
