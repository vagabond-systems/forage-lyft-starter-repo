import unittest
from engine.capulet_engine import CapuletEngine


class CapuletEngineTest(unittest.TestCase):
    def test_engine_should_be_served(self):
        current_mileage = 50000
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_served(self):
        current_mileage = 20000
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

