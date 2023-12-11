#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .tire import Tire

class Carrigan(Tire):
    def needs_service(self, wear):
        return any(i >= 0.9 for i in wear)
