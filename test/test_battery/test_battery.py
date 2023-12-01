#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        nubbin_battery = NubbinBattery()
        self.assertFalse(nubbin_battery.needs_service(2))
        self.assertTrue(nubbin_battery.needs_service(5))

    def test_spindler_battery_needs_service(self):
        spindler_battery = SpindlerBattery()
        self.assertFalse(spindler_battery.needs_service(1))
        self.assertTrue(spindler_battery.needs_service(3))

if __name__ == '__main__':
    unittest.main()
