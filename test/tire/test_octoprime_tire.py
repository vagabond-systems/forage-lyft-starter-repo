import unittest
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        self.assertTrue(OctoprimeTire([0.9, 0.9, 0.3, 0.9]).needs_service())
    def test_tire_should_not_be_serviced(self):
        self.assertFalse(OctoprimeTire([0.1, 0.5, 0.6, 0.3]).needs_service())