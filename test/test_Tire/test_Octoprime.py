import unittest
from car_Module.components.tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_check_needs_service_true_case(self):
        tire = OctoprimeTire([0.9,0.9,1,0.3])
        self.assertTrue(tire.needs_service())

    def test_check_needs_service_flase_case(self):
        tire = OctoprimeTire([0,0.1,0.1,0.2])
        self.assertFalse(tire.needs_service())