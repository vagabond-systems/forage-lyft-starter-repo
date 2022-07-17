import unittest

from engine.sternman_engine import SternmanEngine

class TestStermanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.need_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
       
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.need_service())
        

    