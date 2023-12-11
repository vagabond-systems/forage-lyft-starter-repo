#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Base Battery class """

from servicable import Servicable

class Battery(Servicable):
    def __init__(self, service_criteria):
        self.service_criteria = service_criteria

    def needs_service(self, years):
        return years >= self.service_criteria
