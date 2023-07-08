import unittest

from engine.sternman_engine import SternmanEngine


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced_true(self):
        warning_light_is_on = 1
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced_false(self):
        warning_light_is_on = 0
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == "__main__":
    unittest.main()