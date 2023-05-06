import unittest

from tire.octoprime_tires import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_to_be_serviced(self):
        tire_sensor_readings = [0.2, 0.5, 0.7, 0.1]
        
        service = OctoprimeTire(tire_sensor_readings)
        self.assertTrue(service.needs_service)
