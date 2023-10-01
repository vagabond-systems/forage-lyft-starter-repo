from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def service_needed(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
