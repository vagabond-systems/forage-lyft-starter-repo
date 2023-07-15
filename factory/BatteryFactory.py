from _attempt.battery.IBattery import IBattery
from _attempt.battery.NubbinBattery import NubbinBattery
from _attempt.battery.SpindlerBattery import SpindlerBattery


class BatteryFactory:
    
    def create_battery(battery_type, last_service_date, current_date) -> IBattery:
        if battery_type.capitalize() == 'Spindler':
            return SpindlerBattery(last_service_date, current_date)
        elif battery_type.capitalize() == 'Nubbin':
            return NubbinBattery(last_service_date, current_date)
        else:
            raise ValueError('Wrong battery inputted')

