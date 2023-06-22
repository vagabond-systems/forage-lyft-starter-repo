import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TireTests(unittest.TestCase):
    def test_carrigan_needs_service(self):
        # one or more than one value is greater than or equal to 0.9
        tire_values = [0.9, 0.9, 0.6, 0.6]
        tire = CarriganTire(tire_values)
        self.assertTrue(tire.needs_service())

    def test_carrigan_does_not_need_service(self):
        # none of the values are greater than or equal to 0.9
        tire_values = [0.8, 0.8, 0.7, 0.7]
        tire = CarriganTire(tire_values)
        self.assertFalse(tire.needs_service())

    def test_octoprime_needs_service(self):
        # sum of values >= 3
        tire_values = [0.8, 0.8, 0.8, 0.8]
        tire = OctoprimeTire(tire_values)
        self.assertTrue(tire.needs_service())

    def test_octoprime_does_not_need_service(self):
        # sum of values < 3
        tire_values = [0.6, 0.6, 0.6, 0.6]
        tire = OctoprimeTire(tire_values)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
