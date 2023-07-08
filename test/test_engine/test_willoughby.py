import unittest

from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == "__main__":
    unittest.main()