from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine

class Rorschach(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        # Service criteria for Rorschach: Check if either the engine or battery needs service
        return service_threshold_date < datetime.today().date() or self.needs_service()
