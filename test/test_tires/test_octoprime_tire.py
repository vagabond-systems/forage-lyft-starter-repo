import unittest
from datetime import date, timedelta
from tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_tire_needs_service(self):
        # Tire wear array with the sum exceeding the threshold
        tire_wear_array = [1.2, 0.8, 0.6, 0.5]
        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_octoprime_tire_does_not_need_service(self):
        # Tire wear array with the sum below the threshold
        tire_wear_array = [0.5, 0.6, 0.7, 0.8]

        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())