#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" rorschach module"""
from .car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery

class Rorschach(Car):
    """ Rorschach car class."""
    def __init__(self):
        super().__init__(engine=WilloughbyEngine(), battery=NubbinBattery())
