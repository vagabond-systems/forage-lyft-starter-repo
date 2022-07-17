import unittest
from datetime import datetime


from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine

from battery.NubbinBattery import NubbinBattery
from battery.SplinderBattery import SplinderBattery


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.need_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.need_service())
        
class TestStermanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.need_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
       
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.need_service())
        
class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 70001
        last_service_mileage = 500

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.need_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.need_service())
    
    
class TestNubblinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date, today)
        self.assertIsNone(battery.need_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.need_service())

        
class TestSplinderBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
    

        battery = SplinderBattery(last_service_date, today)
        self.assertIsNone(battery.need_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        
        battery = SplinderBattery(last_service_date, today)
        self.assertFalse(battery.need_service())
    



if __name__ == '__main__':
    unittest.main()
