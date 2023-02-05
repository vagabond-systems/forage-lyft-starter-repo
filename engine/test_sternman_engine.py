import unittest
from sternman_engine import SternmanEngine

class TestSternman(unittest.TestCase):
    def test_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
        
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()