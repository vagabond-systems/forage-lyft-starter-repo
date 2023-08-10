from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self):
         #service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        service_threshold_date = self.warning_light_is_on.replace(miles=self.warning_light_is_on) 
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
