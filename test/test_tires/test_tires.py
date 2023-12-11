#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

class TestTire(unittest.TestCase):
    def test_carrigan_tire_needs_service(self):
        carrigan_tire = Carrigan()
        self.assertFalse(carrigan_tire.needs_service([0.8, 0.7, 0.6, 0.5]))
        self.assertTrue(carrigan_tire.needs_service([0.9, 0.7, 0.6, 0.5]))

    def test_octoprime_tire_needs_service(self):
        octoprime_tire = Octoprime()
        self.assertFalse(octoprime_tire.needs_service([0.8, 0.7, 0.6, 0.5]))
        self.assertTrue(octoprime_tire.needs_service([0.8, 0.7, 0.8, 0.9]))
if __name__ == '__main__':
    unittest.main()
