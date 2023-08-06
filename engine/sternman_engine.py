from abc import ABC

from engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on: bool):
        self.__warning_light_on = warning_light_is_on

    def needs_service(self) -> bool:
        if self.__warning_light_on:
            return True
        else:
            return False
