import unittest
from tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_needs_service(self):
        # Tire wear array with one tire needing service
        tire_wear_array = [0.8, 0.9, 0.85, 0.95]

        tire = CarriganTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_carrigan_tire_does_not_need_service(self):
        # Tire wear array with all tires in good condition
        tire_wear_array = [0.7, 0.6, 0.75, 0.85]

        tire = CarriganTire(tire_wear_array)
        self.assertFalse(tire.needs_service())