from Serviceable import Serviceable


class Car(Serviceable):

    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
