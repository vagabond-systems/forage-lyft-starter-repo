
import unittest
from engine.engine import Engine
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        """ Set up the current mileage and last service mileage"""
        current_mileage = 70000
        last_service_mileage = 10000
        willoughby_engine = WilloughbyEngine(current_mileage,
                                             last_service_mileage)

        result = willoughby_engine.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """ Set up the current mileage and last service mileage"""
        current_mileage = 50000
        last_service_mileage = 40000
        willoughby_engine = WilloughbyEngine(current_mileage,
                                             last_service_mileage)
        result = willoughby_engine.needs_service()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
