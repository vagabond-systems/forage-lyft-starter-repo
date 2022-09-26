import unittest
from datetime import datetime

from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    ## Should be serviced every 30000 miles
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 30000
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    ## Should be serviced only when the warning indicator is on
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    ## Should be serviced every 60000 miles
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 60000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

        
if __name__ == '__main__':
    unittest.main()