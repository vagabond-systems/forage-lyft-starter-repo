#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" glissade car module."""
from .car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery

class Glissade(Car):
    """ Glissade car class."""
    def __init__(self):
        super().__init__(engine=WilloughbyEngine(), battery=SpindlerBattery())
