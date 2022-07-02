import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_condition = [0, 0.5, 0.9, 0]
        tire = CarriganTires(tires_condition)
        self.assertTrue((tire.needs_service()))

    def test_tires_should_not_be_serviced(self):
        tires_condition = [0, 0.5, 0, 0]
        tire = CarriganTires(tires_condition)
        self.assertFalse((tire.needs_service()))


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_condition = [0, 1, 1.5, 1]
        tire = OctoprimeTires(tires_condition)
        self.assertTrue((tire.needs_service()))

    def test_tires_should_not_be_serviced(self):
        tires_condition = [0, 0.5, 0, 0]
        tire = OctoprimeTires(tires_condition)
        self.assertFalse((tire.needs_service()))
