
from engine.engine import Engine


# private variables for class
class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self.__warning_light_on = warning_light_on

    # returns True if warning light is on. Serviced only if warning light is on
    def engine_should_be_serviced(self) -> bool:
        return self.__warning_light_on
