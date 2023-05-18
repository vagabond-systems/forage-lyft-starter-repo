import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class Test_CarriganTires(unittest.TestCase):
    def test_needs_servicing(self):
        tires = CarriganTires(0.95, 0.1, 0.2, 0.5)
        self.assertTrue(tires.needs_service())

    def test_does_not_need_servicing(self):
        tires = CarriganTires(0.2, 0.3, 0.4, 0.1)
        self.assertFalse(tires.needs_service())

class Test_OctoprimeTires(unittest.TestCase):
    def test_needs_servicing(self):
        tires = OctoprimeTires(0.95, 0.9, 0.8, 0.7)
        self.assertTrue(tires.needs_service())

    def test_does_not_need_servicing(self):
        tires = OctoprimeTires(0.2, 0.3, 0.4, 0.1)
        self.assertFalse(tires.needs_service())
