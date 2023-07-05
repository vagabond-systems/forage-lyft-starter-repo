import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarTestCase(unittest.TestCase):
    def setUp(self):
        # Set up common variables for test cases
        self.today = datetime.today().date()
        self.last_service_date = self.today.replace(year=self.today.year - 1)
        self.current_mileage = 0
        self.last_service_mileage = 0

    def test_calliope_battery_should_be_serviced(self):
        # Test if Calliope battery needs to be serviced
        car = Calliope(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_calliope_battery_should_not_be_serviced(self):
        # Test if Calliope battery does not need to be serviced
        car = Calliope(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_calliope_engine_should_be_serviced(self):
        # Test if Calliope engine needs to be serviced
        self.current_mileage = 30001
        car = Calliope(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_calliope_engine_should_not_be_serviced(self):
        # Test if Calliope engine does not need to be serviced
        self.current_mileage = 30000
        car = Calliope(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_glissade_battery_should_be_serviced(self):
        # Test if Glissade battery needs to be serviced
        car = Glissade(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_battery_should_not_be_serviced(self):
        # Test if Glissade battery does not need to be serviced
        car = Glissade(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_glissade_engine_should_be_serviced(self):
        # Test if Glissade engine needs to be serviced
        self.current_mileage = 60001
        car = Glissade(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_engine_should_not_be_serviced(self):
        # Test if Glissade engine does not need to be serviced
        self.current_mileage = 60000
        car = Glissade(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

  
    def test_palindrome_battery_should_be_serviced(self):
        # Test if Palindrome battery needs to be serviced
        self.last_service_date = self.today.replace(year=self.today.year - 5)
        warning_light_is_on = False
        car = Palindrome(self.last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_palindrome_battery_should_not_be_serviced(self):
        # Test if Palindrome battery does not need to be serviced
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        warning_light_is_on = False
        car = Palindrome(self.last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_palindrome_engine_should_be_serviced(self):
        # Test if Palindrome engine needs to be serviced
        warning_light_is_on = True
        car = Palindrome(self.last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_palindrome_engine_should_not_be_serviced(self):
        # Test if Palindrome engine does not need to be serviced
        warning_light_is_on = False
        car = Palindrome(self.last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_rorschach_battery_should_be_serviced(self):
        # Test if Rorschach battery needs to be serviced
        self.last_service_date = self.today.replace(year=self.today.year - 5)
        self.current_mileage = 0
        self.last_service_mileage = 0
        car = Rorschach(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_rorschach_battery_should_not_be_serviced(self):
        # Test if Rorschach battery does not need to be serviced
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 0
        self.last_service_mileage = 0
        car = Rorschach(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_rorschach_engine_should_be_serviced(self):
        # Test if Rorschach engine needs to be serviced
        self.current_mileage = 60001
        car = Rorschach(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_rorschach_engine_should_not_be_serviced(self):
        # Test if Rorschach engine does not need to be serviced
        self.current_mileage = 60000
        car = Rorschach(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_thovex_battery_should_be_serviced(self):
        # Test if Thovex battery needs to be serviced
        self.last_service_date = self.today.replace(year=self.today.year - 5)
        self.current_mileage = 0
        self.last_service_mileage = 0
        car = Thovex(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_battery_should_not_be_serviced(self):
        # Test if Thovex battery does not need to be serviced
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 0
        self.last_service_mileage = 0
        car = Thovex(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_thovex_engine_should_be_serviced(self):
        # Test if Thovex engine needs to be serviced
        self.current_mileage = 30001
        car = Thovex(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_engine_should_not_be_serviced(self):
        # Test if Thovex engine does not need to be serviced
        self.current_mileage = 30000
        car = Thovex(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
