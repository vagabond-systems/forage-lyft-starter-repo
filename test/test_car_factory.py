import unittest
from car_factory import CarFactory

class TestCarFactory(unittest.TestCase):
    def test_create_calliope_with_carrigan_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_calliope(tire_wear)
        self.assertTrue(car.needs_service())

    def test_create_calliope_with_octoprime_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_calliope(tire_wear)
        self.assertFalse(car.needs_service())

    def test_create_glissade_with_carrigan_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_glissade(tire_wear)
        self.assertTrue(car.needs_service())

    def test_create_glissade_with_octoprime_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_glissade(tire_wear)
        self.assertFalse(car.needs_service())

    def test_create_palindrome_with_carrigan_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_palindrome(tire_wear)
        self.assertTrue(car.needs_service())

    def test_create_palindrome_with_octoprime_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_palindrome(tire_wear)
        self.assertFalse(car.needs_service())

    def test_create_rorschach_with_carrigan_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_rorschach(tire_wear)
        self.assertTrue(car.needs_service())

    def test_create_rorschach_with_octoprime_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_rorschach(tire_wear)
        self.assertFalse(car.needs_service())

    def test_create_thovex_with_carrigan_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_thovex(tire_wear)
        self.assertTrue(car.needs_service())

    def test_create_thovex_with_octoprime_tires(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        car = CarFactory.create_thovex(tire_wear)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
