from datetime import datetime

from nubbin_Battery import NubbinBattery


class Thovex(NubbinBattery):
    def needs_service(self):
         #service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced():
            return True
        else:
            return False

