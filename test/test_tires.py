import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def setUp(self):
        # Carrigan tires must be serviced if any of the tires wear is >= 0.9
        self.carrigan_tires_that_need_service = CarriganTires((0.8, 0.9, 1, 0.8))
        self.carrigan_tires_that_dont_need_service = CarriganTires((0.1, 0, 0.2, 0.1))

    def test_should_need_service(self):
        self.assertTrue(
            self.carrigan_tires_that_need_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.carrigan_tires_that_dont_need_service.needs_service()
        )


class TestOctoprimeTires(unittest.TestCase):
    def setUp(self):
        # Octoprime tires must be serviced if the sum of all tires wear is >= 3.
        self.octoprime_tires_that_need_service = OctoprimeTires((0.8, 0.9, 1, 0.8))
        self.octoprime_tires_that_dont_need_service = OctoprimeTires((0.7, 0.8, 0.7, 0.7))

    def test_should_need_service(self):
        self.assertTrue(
            self.octoprime_tires_that_need_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.octoprime_tires_that_dont_need_service.needs_service()
        )