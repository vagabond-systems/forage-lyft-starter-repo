from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(WilloughbyEngine,NubbinBattery):
    def needs_service(self):
        if self.battery_should_be_serviced or self.engine_should_be_serviced():
            return True
        else:
            return False
