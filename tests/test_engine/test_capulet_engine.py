
import unittest
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        """ Set up the current mileage and last service mileage """
        current_mileage = 35000
        last_service_mileage = 5000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        result = capulet_engine.needs_service()
        self.assertTrue(result)

    def test_needs_service_false(self):
        """ Set up the current mileage and last service mileage """
        current_mileage = 25000
        last_service_mileage = 20000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        result = capulet_engine.needs_service()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
