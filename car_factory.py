#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan import Carrigan
from tires.octoprime import OctoPrime

class CarFactory:
    def create_calliope(tire):
        return Calliope(
            engine=CapuletEngine(),
            battery=SpindlerBattery(),
            tire=tire
        )

    @staticmethod
    def create_glissade(tire):
        return Glissade(
            engine=SternmanEngine(),
            battery=SpindlerBattery(),
            tire=tire
        )

    @staticmethod
    def create_palindrome(tire):
        return Palindrome(
            engine=SternmanEngine(),
            battery=SpindlerBattery(),
            tire=tire
        )

    @staticmethod
    def create_rorschach(tire):
        return Rorschach(
            engine=CapuletEngine(),
            battery=NubbinBattery(),
            tire=tire
        )

    @staticmethod
    def create_thovex(tire):
        return Thovex(
            engine=CapuletEngine(),
            battery=NubbinBattery(),
            tire=tire
        )            
