from engine.engine import Engine


class CapuletEngine(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.capulet_mileage_need_service = 3000

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > self.capulet_mileage_need_service
