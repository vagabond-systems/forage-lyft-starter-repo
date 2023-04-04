from datetime import datetime
import unittest

from Serviceable.Car import Car


from CarFactory.CarFactory import CarFactory 

class TestCallopie(unittest.TestCase):
    # Engine needs servicing
    def testCallopie_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 30001
        last_service_mileage = 0
        car = CarFactory.create_callopie(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Battery needs servicing
    def testCallopie_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 29999
        last_service_mileage = 0
        car = CarFactory.create_callopie(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Car does not need servicing
    def testCallopie_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 29999
        last_service_mileage = 0
        car = CarFactory.create_callopie(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    # Engine needs servicing
    def testGlissade_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 60001
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Battery needs servicing
    def testGlissade_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 59999
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Car does not need servicing
    def testGlissade_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 59999
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    # Engine needs servicing
    def testPalindrome_engine_should_be_serviced(self):
        warning_light_is_on = True
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        car = CarFactory.create_palindrome(current_date, last_service_date,warning_light_is_on)

        self.assertTrue(car.needs_service())

    # Battery needs servicing
    def testPalindrome_battery_should_be_serviced(self):
        warning_light_is_on = False
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        car = CarFactory.create_palindrome(current_date, last_service_date,warning_light_is_on)

        self.assertTrue(car.needs_service())

    # Car does not need servicing
    def testPalindrome_should_not_be_serviced(self):
        warning_light_is_on = False
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        car = CarFactory.create_palindrome(current_date, last_service_date,warning_light_is_on)

        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    # Engine needs servicing
    def testGlissade_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 60001
        last_service_mileage = 0
        car = CarFactory.create_rorschach(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Battery needs servicing
    def testGlissade_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 59999
        last_service_mileage = 0
        car = CarFactory.create_rorschach(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Car does not need servicing
    def testGlissade_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 59999
        last_service_mileage = 0
        car = CarFactory.create_rorschach(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    # Engine needs servicing
    def testThovex_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 30001
        last_service_mileage = 0
        car = CarFactory.create_thovex(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Battery needs servicing
    def testThovex_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 29999
        last_service_mileage = 0
        car = CarFactory.create_thovex(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(car.needs_service())

    # Car does not need servicing
    def testThovex_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 29999
        last_service_mileage = 0
        car = CarFactory.create_thovex(current_date, last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(car.needs_service())

    if __name__ == '__main__':
        unittest.main()