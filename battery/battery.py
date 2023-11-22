#!/usr/bin/python3
"""defines battery module"""
from abc import ABC


class Battery(ABC):
    def needs_service(self):
        pass
