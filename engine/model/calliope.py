from datetime import datetime
from engine.capulet_engine import CapuletEngine

class Calliope(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        # Service criteria for Calliope: Check if either the engine or battery needs service
        return service_threshold_date < datetime.today().date() or self.needs_service()
