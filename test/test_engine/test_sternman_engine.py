
import unittest
from engine.engine import Engine
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        """ Create a SternmanEngine instance with the warning light on"""
        sternman_engine = SternmanEngine(warning_light_is_on=True)
        result = sternman_engine.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """ Create a SternmanEngine instance with the warning light off"""
        sternman_engine = SternmanEngine(warning_light_is_on=False)
        result = sternman_engine.needs_service()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
