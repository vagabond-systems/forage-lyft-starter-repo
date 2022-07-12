import unittest
import tire
from datetime import datetime

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_sensor_readings = [0.9, 0.3, 0.4, 0.4]
        tire = CarriganTire(tire_sensor_readings)
        self.assertTrue(tire)

    def test_tire_should_not_be_serviced(self):
        tire_sensor_readings = [0.1, 0.3, 0.4, 0.4]
        tire = CarriganTire(tire_sensor_readings)
        self.assertFalse(tire)


class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_sensor_readings = [1, 1, 0.4, 1]
        tire = CarriganTire(tire_sensor_readings)
        self.assertTrue(tire)

    def test_tire_should_not_be_serviced(self):
        tire_sensor_readings = [0.1, 0.3, 0.4, 0.4]
        tire = CarriganTire(tire_sensor_readings)
        self.assertFalse(tire)
