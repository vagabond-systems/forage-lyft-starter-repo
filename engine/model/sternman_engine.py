from engine.engine import Engine
from datetime import datetime



class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on


    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False 


    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
