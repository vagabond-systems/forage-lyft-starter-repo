#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestEngine(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        capulet_engine = CapuletEngine()
        self.assertFalse(capulet_engine.needs_service(2000))
        self.assertTrue(capulet_engine.needs_service(40000))

    def test_sternman_engine_needs_service(self):
        sternman_engine = SternmanEngine()
        self.assertFalse(sternman_engine.needs_service(25000))

    def test_willoughby_engine_needs_service(self):
        willoughby_engine = WilloughbyEngine()
        self.assertFalse(willoughby_engine.needs_service(25000))
        self.assertTrue(willoughby_engine.needs_service(70000))

if __name__ == '__main__':
    unittest.main()

