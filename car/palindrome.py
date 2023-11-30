#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" palindrome module"""
from .car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(Car):
    """ Palindrome car class."""
    def __init__(self):
        super().__init__(engine=SternmanEngine(), battery=SpindlerBattery())
