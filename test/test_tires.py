import unittest

from tire.CarriganTire import CarriganTire
from tire.OctoprimeTire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_should_be_serviced(self):
        tires_array = [0.9, 0.8, 0.7, 0.6]
        carrigan_tire = CarriganTire(tires_array)

        self.assertTrue(carrigan_tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        tires_array = [0.8, 0.7, 0.6, 0.5]
        carrigan_tire = CarriganTire(tires_array)

        self.assertFalse(carrigan_tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_tire_should_be_serviced(self):
        tires_array = [0.9, 0.8, 0.7, 0.6]
        octoprime_tire = OctoprimeTire(tires_array)

        self.assertTrue(octoprime_tire.needs_service())

    def test_octoprime_tire_should_not_be_serviced(self):
        tires_array = [0.8, 0.7, 0.6, 0.5]
        octoprime_tire = OctoprimeTire(tires_array)

        self.assertFalse(octoprime_tire.needs_service())