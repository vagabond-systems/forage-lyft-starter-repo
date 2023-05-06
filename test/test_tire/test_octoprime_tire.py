import unittest

from tire.octoprime_tires import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_to_be_serviced(self):
        tire_sensor_readings = [0.9, 0.9, 0.7, 0.1]
        
        service = OctoprimeTire(tire_sensor_readings)
        self.assertTrue(service.needs_service)
        
    def test_does_not_need_service(self):
        tire_sensor_readings = [0.3, 0.5, 0.7, 0.1]
        
        service = OctoprimeTire(tire_sensor_readings)
        self.assertFalse(service.needs_service)
