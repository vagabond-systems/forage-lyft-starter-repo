import unittest

from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.9, 0.6, 0.5, 0.4]
        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service(sensors))

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_false(self):
        sensors = [0.2, 0.6, 0.5, 0.4]
        tire = CarriganTire(sensors)
        self.assertFalse(tire.needs_service(sensors))