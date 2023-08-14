import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tirewearreading = [0.8, 0.6, 0.9, 0.7]
        tires = OctoprimeTires(tirewearreading)
        self.assertTrue(tires.needs_service())

    def test_battery_should_not_be_serviced(self):
        tirewearreading = [0.3, 0.3, 0.2, 0.2]
        tires = OctoprimeTires(tirewearreading)
        self.assertFalse(tires.needs_service())

