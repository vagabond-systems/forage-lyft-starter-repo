import unittest
from datetime import datetime
from engine.sternman_engine import SternmanEngine

class CapuletEngineTest(unittest.TestCase):
    def test_engine_should_be_served(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_served(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())  