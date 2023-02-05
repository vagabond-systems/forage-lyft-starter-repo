import unittest
from willoughby_engine import WilloughbyEngine

class TestWilloughby(unittest.TestCase):
    def test_needs_service(self):
        engine = WilloughbyEngine(61000, 0)
        self.assertTrue(engine.needs_service())
        
        engine = WilloughbyEngine(60000, 0)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()