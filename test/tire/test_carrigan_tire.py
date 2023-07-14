import unittest
from tire.carrigan_tire import CarriganTire


class CarriganTireTest(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        sensors = [0.1,0.4,0.6,0.9]
        tire = CarriganTire(sensors)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0.1,0.4,0.6,0.3]
        tire = CarriganTire(sensors)

        self.assertFalse(tire.needs_service()) 