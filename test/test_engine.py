import unittest

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())



class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        car = SternmanEngine(warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


    