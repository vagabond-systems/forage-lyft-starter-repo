import unittest
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_changed(self):
        tire_wear = [0.9, 0.9, 1, 1]
        tire = OctoprimeTires(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_changed(self):
        tire_wear = [0.4, 0.8, 0.4, 0.5]
        tire = OctoprimeTires(tire_wear)
        self.assertFalse(tire.needs_service())
