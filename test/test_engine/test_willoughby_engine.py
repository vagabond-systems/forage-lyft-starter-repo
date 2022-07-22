import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 70001
        last_service_mileage = 500

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.need_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.need_service())