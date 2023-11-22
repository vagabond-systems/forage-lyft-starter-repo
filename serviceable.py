#!/usr/bin/python3
"""Defines Serviceable.py"""
from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
