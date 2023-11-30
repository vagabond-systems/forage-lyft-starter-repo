#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" spindler battery module"""
from .battery import Battery

class SpindlerBattery(Battery):
    def __init__(self):
        super().__init__(service_criteria=2)
