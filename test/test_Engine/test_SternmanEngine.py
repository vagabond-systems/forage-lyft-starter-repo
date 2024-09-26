import unittest
from car_Module.components.engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_check_needs_service_true_case(self):
        capulet = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(capulet.needs_service())

    def test_check_needs_service_false_case(self):
        capulet = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(capulet.needs_service())