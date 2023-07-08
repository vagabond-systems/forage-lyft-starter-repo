import unittest
from tyre.carrigan_tyre import CarriganTyre


class TestCarrigan(unittest.TestCase):
    def test_carrigan_service_true(self):
        worn_counts = [0.2, 0.9, 0.5, 0.8]
        tyre = CarriganTyre(worn_counts)
        self.assertTrue(tyre.tyres_needs_service())


    def test_carrigan_service_false(self):
        worn_counts = [0.2, 0.7, 0.5, 0.8]
        tyre = CarriganTyre(worn_counts)
        self.assertFalse(tyre.tyres_needs_service())


if __name__ == "__main__":
    unittest.main()
