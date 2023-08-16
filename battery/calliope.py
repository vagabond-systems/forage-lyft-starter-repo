<<<<<<< HEAD
from datetime import datetime
from spinder_Battery import SpinderBattery

class Calliope(SpinderBattery):
    def needs_service(self,):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced():
            return True
        else:
            return False

=======
from datetime import datetime
from spinder_Battery import SpinderBattery

class Calliope(SpinderBattery):
    def needs_service(self,):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced():
            return True
        else:
            return False

>>>>>>> 9bc8b7485f6b0894923ea1f036023985f5acf3b9
    