from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def requires_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        mileage_service = self.requires_engine_service()
        if service_threshold_date < datetime.today().date() or mileage_service:
            return True
        else:
            return False
