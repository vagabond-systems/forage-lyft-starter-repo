from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        """
        Check if the Calliope engine needs to be serviced.

        Returns:
        bool: True if the engine needs service, False otherwise.
        """
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        
        # Check if the service threshold date is earlier than today's date or if the engine should be serviced
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
