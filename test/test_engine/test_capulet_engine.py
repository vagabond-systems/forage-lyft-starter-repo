import unittest
from engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 0
        current_mileage = 30005

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 20000

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())