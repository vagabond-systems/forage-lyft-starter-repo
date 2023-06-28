from engine2.engine import Engine


class WiloughByEngine(Engine):
    def __init__(self, current_milage, last_service_milage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_milage

    def need_services(self):
        return self.current_milage - self.last_service_milage > 30000
