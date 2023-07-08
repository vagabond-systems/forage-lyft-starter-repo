import unittest
from tyre.octoprime_tyre import OctoprimeTyre

class TestOctoprime(unittest.TestCase):
    def test_octoprime_service_true(self):
        worn_counts = [0.9, 0.9, 0.9, 0.8]
        tyre = OctoprimeTyre(worn_counts)
        self.assertTrue(tyre.tyres_needs_service())


    def test_octoprime_service_false(self):
        worn_counts = [0.2, 0.7, 0.5, 0.8]
        tyre = OctoprimeTyre(worn_counts)
        self.assertFalse(tyre.tyres_needs_service())


if __name__ == "__main__":
    unittest.main()