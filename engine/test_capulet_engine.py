import unittest
from capulet_engine import CapuletEngine

class TestCapulet(unittest.TestCase):
    def test_needs_service(self):
        engine = CapuletEngine(31000, 0)
        self.assertTrue(engine.needs_service())
        
        engine = CapuletEngine(30000, 0)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()