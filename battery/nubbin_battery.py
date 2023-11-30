#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" nubbin battery module"""
from .battery import Battery

class NubbinBattery(Battery):
    def __init__(self):
        super().__init__(service_criteria=4)
