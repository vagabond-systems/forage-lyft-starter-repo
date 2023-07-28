import unittest
from engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 0
        current_mileage = 60005

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 60000

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())