import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [1, 0.5, 0.5, 1]
        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service(sensors))

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_false(self):
        sensors = [0.2, 0.3, 0.5, 0.4]
        tire = OctoprimeTire(sensors)
        self.assertFalse(tire.needs_service(sensors))