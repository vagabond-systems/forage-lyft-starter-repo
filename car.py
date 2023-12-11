#!/usr/bin/env python
# -*- coding: utf-8 -*-

from servicable import Servicable


class Car(Servicable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery

    def needs_service(self, mileage, years) -> bool:
        return self.engine.needs_service(mileage) or self.battery.needs_service(years)
