import unittest

from tires.octoprime_tire import OctoprimeTire


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.6, 0.4, 1.8, 0.7]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())