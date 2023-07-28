import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_changed(self):
        tire_wear = [0.4, 0.9, 1, 0.5]
        tire = CarriganTires(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_changed(self):
        tire_wear = [0.4, 0.8, 0.4, 0.5]
        tire = CarriganTires(tire_wear)
        self.assertFalse(tire.needs_service())
