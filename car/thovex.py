#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" thovex module"""
from .car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery

class Thovex(Car):
    """ Thovex car class."""
    def __init__(self):
        super().__init__(engine=CapuletEngine(), battery=NubbinBattery())
