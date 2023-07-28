
from engine.engine import Engine


# serviced only if the warning light is on
class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self.__warning_light_on = warning_light_on

    # returns true if the warning light is on
    def needs_service(self) -> bool:
        return self.__warning_light_on
