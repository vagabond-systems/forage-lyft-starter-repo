<<<<<<< HEAD
from datetime import datetime
import unittest
from engine.sternman_engine import SternmanEngine

class TestStermanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        car = SternmanEngine(warning_light_is_on)
=======
from datetime import datetime
import unittest
from engine.sternman_engine import SternmanEngine

class TestStermanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        car = SternmanEngine(warning_light_is_on)
>>>>>>> 62d5fc9d0ca056c4f81add711b54c9f2533665ba
        self.assertFalse(car.needs_service())