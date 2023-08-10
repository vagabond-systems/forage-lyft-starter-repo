from datetime import datetime
from spinder_Battery import SpinderBattery

class Glissade(SpinderBattery):
    def needs_service(self,):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced():
            return True
        else:
            return False

    