import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tirewearreading = [0.3, 0.5, 0.9, 0.1]
        tires = CarriganTires(tirewearreading)
        self.assertTrue(tires.needs_service())

    def test_battery_should_not_be_serviced(self):
        tirewearreading = [0.3, 0.3, 0.2, 0.2]
        tires = CarriganTires(tirewearreading)
        self.assertFalse(tires.needs_service())

