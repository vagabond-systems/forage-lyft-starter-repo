import unittest
from car_Module.components.tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_check_needs_service_true_case(self):
        tire = CarriganTire([0,0.9,1,0.2])
        self.assertTrue(tire.needs_service())

    def test_check_needs_service_flase_case(self):
        tire = CarriganTire([0,0.1,0.1,0.2])
        self.assertFalse(tire.needs_service())