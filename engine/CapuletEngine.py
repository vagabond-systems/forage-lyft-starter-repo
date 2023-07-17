from engine.IEngine import IEngine


class CapuletEngine(IEngine):

    def __init__(self, last_service_date, last_service_mileage, current_mileage):
        super().__init__(last_service_date)
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        mileage_difference = self.current_mileage - self.last_service_mileage
        if mileage_difference < 0:
            raise ValueError('Mileage difference should not be negative')
        else:
            return mileage_difference >= 30000

