from battery.battery_interface import BatteryInterface

class NubbinBattery(BatteryInterface):

    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service():
        pass    