import unittest
from engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        warning_light_on = False

        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())