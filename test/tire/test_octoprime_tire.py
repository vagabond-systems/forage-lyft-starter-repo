import unittest
from tire.octoprime_tire import OctoprimeTire


class OctoprimeTireTest(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        sensors = [0.7,0.9,0.8,0.9]
        tire = OctoprimeTire(sensors)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0.1,0.4,0.6,0.3]
        tire = OctoprimeTire(sensors)

        self.assertFalse(tire.needs_service()) 