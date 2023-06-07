import unittest
from datetime import date
from willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        # Test case where service is needed
        engine = WilloughbyEngine(5000, 70000)
        self.assertTrue(engine.needs_service())

        # Test case where service is not needed
        engine = WilloughbyEngine(5000, 55000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
