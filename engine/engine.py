#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Base engine class."""

from servicable import Servicable

class Engine(Servicable):
    def __init__(self, service_criteria):
        self.service_criteria = service_criteria

    def needs_service(self, mileage):
        return mileage >= self.service_criteria
