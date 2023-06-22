import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class EngineTests(unittest.TestCase):
    def test_capulet_needs_service(self):
        current_mileage = 150000
        last_service_mileage = 120000
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_capulet_does_not_need_service(self):
        current_mileage = 150000
        last_service_mileage = 130000
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())

    def test_sternman_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.needs_service())

    def test_sternman_does_not_need_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        self.assertFalse(engine.needs_service())

    def test_willoughby_needs_service(self):
        current_mileage = 150000
        last_service_mileage = 90000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_willoughby_does_not_need_service(self):
        current_mileage = 150000
        last_service_mileage = 100000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
