import unittest
from sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        # Test case where service is needed
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

        # Test case where service is not needed
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
