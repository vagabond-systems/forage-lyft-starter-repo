import unittest
from datetime import datetime

from car.calliope import Calliope
from car.glissade import Glissade
from car.palindrome import Palindrome
from car.rorschach import Rorschach
from car.thovex import Thovex


class TestCarService(unittest.TestCase):
    def test_calliope_needs_service(self):
        calliope_car = Calliope()
        self.assertFalse(calliope_car.needs_service(mileage=25000, years=1))
        self.assertTrue(calliope_car.needs_service(mileage=35000, years=3))

    def test_glissade_needs_service(self):
        glissade_car = Glissade()
        self.assertFalse(glissade_car.needs_service(mileage=50000, years=1))
        self.assertTrue(glissade_car.needs_service(mileage=70000, years=4))

    def test_palindrome_needs_service(self):
        palindrome_car = Palindrome()
        self.assertFalse(palindrome_car.needs_service(mileage=15000, years=1))
        self.assertTrue(palindrome_car.needs_service(mileage=20000, years=5))

    def test_rorschach_needs_service(self):
        rorschach_car = Rorschach()
        self.assertFalse(rorschach_car.needs_service(mileage=45000, years=1))
        self.assertTrue(rorschach_car.needs_service(mileage=60000, years=6))

    def test_thovex_needs_service(self):
        thovex_car = Thovex()
        self.assertFalse(thovex_car.needs_service(mileage=29000, years=3))
        self.assertTrue(thovex_car.needs_service(mileage=40000, years=4))


if __name__ == '__main__':
    unittest.main()
