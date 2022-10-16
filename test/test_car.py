import unittest
from datetime import datetime


from engine.battery import spindler_battery
from engine.battery import nubbin_battery

class Testspindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        bat =spindler(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        bat = spindler(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(bat.needs_service())
        
class Testnubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        bat = nubbin(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        bat = nubbin(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(bat.needs_service())


 class Testcapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        
        current_mileage = 30000
        last_service_mileage = 0

        bat = capulet( current_mileage, last_service_mileage)
        self.assertTrue(bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
       
        current_mileage = 0
        last_service_mileage = 0

        bat = capulet( current_mileage, last_service_mileage)
        self.assertFalse(bat.needs_service())
        
 class Teststernman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        
        self.warning_light_is_on = warning_light_is_on

        bat =sternman(warning_light_is_on)
        self.assertTrue(bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
       
        self.warning_light_is_off = warning_light_is_off

        bat =sternman(warning_light_is_off)
       
        self.assertFalse(bat.needs_service())
        
 class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        
        current_mileage = 60000
        last_service_mileage = 0

        bat = capulet( current_mileage, last_service_mileage)
        self.assertTrue(bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
       
        current_mileage = 0
        last_service_mileage = 0

        bat = capulet( current_mileage, last_service_mileage)
        self.assertFalse(bat.needs_service())






if __name__ == '__main__':
    unittest.main()
