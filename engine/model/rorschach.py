from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def requires_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.requires_engine_service():
            return True
        else:
            return False
