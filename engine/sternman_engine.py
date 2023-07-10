from engine import Engine


class SternmanEngine(Engine):
    def __init__(self, waning_light_on):
        self.waning_light_on = waning_light_on

    def needs_service(self):
        if self.waning_light_on:
            return True
        else: 
            return False
        