import unittest

from tire.carriganTire import CarriganTire
from tire.octoPrimeTire import OctoPrimeTire


class CarriganTireTest(unittest.TestCase):
    def test_tire_need_no_service(self):
        sensors = [0.1, 0.3, 0.2, 0.1]

        tire = CarriganTire(sensors)
        self.assertFalse(tire.needs_service())

    def test_tire_need_service(self):
        sensors = [0.9, 0.3, 0.2, 0.1]

        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())


class OctoPrimeTireTest(unittest.TestCase):
    def test_tire_need_no_service(self):
        sensors = [1, 0.4, 0.2, 0.1]
        tire = OctoPrimeTire(sensors)
        self.assertFalse(tire.needs_service())

    def test_tire_need_service(self):
        sensors = [0.9, 1, 2, 0.1]
        tire = OctoPrimeTire(sensors)
        self.assertTrue(tire.needs_service())
