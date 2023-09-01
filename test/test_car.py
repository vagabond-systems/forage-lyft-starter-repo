import unittest
from datetime import datetime
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def assertCarNeedsService(self, car, expected_result):
        self.assertEqual(car.needs_service(), expected_result)

class TestCalliope(CarTestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30001
        last_service_mileage = 0
        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30000
        last_service_mileage = 0
        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

class TestGlissade(CarTestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        current_mileage = 60001
        last_service_mileage = 0
        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        current_mileage = 60000
        last_service_mileage = 0
        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

class TestPalindrome(CarTestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        warning_light_is_on = False
        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertCarNeedsService(car, True)

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        warning_light_is_on = False
        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertCarNeedsService(car, False)

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        warning_light_is_on = True
        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertCarNeedsService(car, True)

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        warning_light_is_on = False
        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertCarNeedsService(car, False)

class TestRorschach(CarTestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        current_mileage = 60001
        last_service_mileage = 0
        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        current_mileage = 60000
        last_service_mileage = 0
        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

class TestThovex(CarTestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30001
        last_service_mileage = 0
        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30000
        last_service_mileage = 



# UNIT TEST

class TestThovex(CarTestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30001
        last_service_mileage = 0
        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, True)

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        current_mileage = 30000
        last_service_mileage = 0
        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertCarNeedsService(car, False)

if __name__ == '__main__':
    unittest.main()