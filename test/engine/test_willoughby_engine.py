<<<<<<< HEAD
from datetime import datetime
import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 59999
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
=======
from datetime import datetime
import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 59999
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
>>>>>>> 62d5fc9d0ca056c4f81add711b54c9f2533665ba
        self.assertFalse(car.needs_service())