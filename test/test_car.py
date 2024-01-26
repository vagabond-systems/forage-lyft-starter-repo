import unittest
from datetime import datetime


from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.5, .3, .2, 0]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.2, .3, .2, .1]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        wornArr = [0, 0, 0, 0]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        wornArr = [0, 0, 0, 0]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.5, .3, .2, 0]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.2, .3, .2, .1]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        wornArr = [0, 0, 0, 0]
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            today, last_service_date, warning_light_is_on, wornArr)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        wornArr = [0, 0, 0, 0]
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            today, last_service_date, warning_light_is_on, wornArr)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        warning_light_is_on = True

        car = CarFactory.create_palindrome(
            last_service_date, last_service_date, warning_light_is_on, wornArr)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            last_service_date, last_service_date, warning_light_is_on, wornArr)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.5, .3, .2, 0]
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            last_service_date, last_service_date, warning_light_is_on, wornArr)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.2, .3, .2, .1]
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            last_service_date, last_service_date, warning_light_is_on, wornArr)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        wornArr = [0, 0, 0, 0]
        current_mileage = 0
        last_service_mileage = 0
        # current_date, last_service_date, current_mileage, last_service_mileage
        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        wornArr = [0, 0, 0, 0]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.5, .3, 2, 1]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.2, .3, .2, .2]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

# current_date, last_service_date, current_mileage, last_service_mileage


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        wornArr = [0, 0, 0, 0]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        wornArr = [0, 0, 0, 0]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        wornArr = [0, 0, 0, 0]
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.5, .3, 2, 1]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wornArr = [.2, .3, .2, .2]
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            last_service_date, last_service_date, current_mileage, last_service_mileage, wornArr)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
