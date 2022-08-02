from abc import ABC

from engine import Engine

class SternmanEngine(Engine, ABC):
    _warning_light_is_on

    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self._warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

    def needs_service(self):
        pass
