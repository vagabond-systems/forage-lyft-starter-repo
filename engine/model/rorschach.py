from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        """
        Check if the Rorschach engine needs to be serviced.

        Returns:
        bool: True if the engine needs service, False otherwise.
        """
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        
