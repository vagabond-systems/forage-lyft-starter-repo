import unittest
from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        self.assertTrue(CarriganTire([0.1, 0.9, 0.2, 0.9]).needs_service())
    def test_tire_should_not_be_serviced(self):
        self.assertFalse(CarriganTire([0.1, 0.5, 0.6, 0.3]).needs_service())