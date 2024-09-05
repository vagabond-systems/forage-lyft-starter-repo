import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestTires(unittest.TestCase):
    def test_carrigan_tires_should_be_serviced(self):
        tire_wear = [0.2, 0.9, 0.4, 0.3]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tire_wear = [0.2, 0.7, 0.4, 0.3]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())

    def test_octoprime_tires_should_be_serviced(self):
        tire_wear = [0.9, 0.8, 0.7, 0.6]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_octoprime_tires_should_not_be_serviced(self):
        tire_wear = [0.5, 0.6, 0.7, 0.8]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
