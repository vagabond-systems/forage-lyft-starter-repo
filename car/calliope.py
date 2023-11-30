#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" calliope car module."""

from .car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery

class Calliope(Car):
    """ Calliope car class."""
    def __init__(self):
        super().__init__(engine=CapuletEngine(), battery=SpindlerBattery())
