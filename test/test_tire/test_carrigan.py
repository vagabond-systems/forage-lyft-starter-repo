import unittest

from tires.carrigan_tire import CarriganTire


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.5, 0.2, 0.4, 1.2]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.7, 0.4, 0.1, 0.8]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())