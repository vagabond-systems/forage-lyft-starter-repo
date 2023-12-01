#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .tire import Tire

class Octoprime(Tire):
    def needs_service(self, wear):
        return sum(wear) >= 3
