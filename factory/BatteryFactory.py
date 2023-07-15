from battery.IBattery import IBattery
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery


class BatteryFactory:
    
    def create_battery(battery_type, last_service_date, current_date) -> IBattery:
        if battery_type.capitalize() == 'Spindler':
            return SpindlerBattery(last_service_date, current_date)
        elif battery_type.capitalize() == 'Nubbin':
            return NubbinBattery(last_service_date, current_date)
        else:
            raise ValueError('Wrong battery inputted')

