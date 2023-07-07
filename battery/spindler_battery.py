from battery.battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    
    def battery_should_be_serviced(self):
        today = datetime.today().date()
        Service_year_for_spindler = 2
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + Service_year_for_spindler)
        if service_threshold_date < today:
            return True
        else:
            return False

# last_service_date = datetime(2020,5, 17).date()
# palindrome = SpindlerBattery(last_service_date)
# print(palindrome.battery_should_be_serviced())