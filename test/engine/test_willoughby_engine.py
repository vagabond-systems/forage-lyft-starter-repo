import unittest
from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine

class CapuletEngineTest(unittest.TestCase):
    def test_engine_should_be_served(self):
        current_mileage = 80000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_served(self):
        current_mileage = 20000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())  