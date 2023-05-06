import unittest

from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_to_be_serviced(self):
        tire_sensor_readings = [0.2, 0.5, 0.9, 0.1]
        
        service = CarriganTire(tire_sensor_readings)
        self.assertTrue(service.needs_service)

    def test_does_not_need_to_be_serviced(self):
        tire_sensor_readings = [0.2, 0.5, 0.7, 0.1]
        
        service = CarriganTire(tire_sensor_readings)
        self.assertFalse(service.needs_service)