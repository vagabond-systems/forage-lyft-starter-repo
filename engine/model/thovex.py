from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery



class Thovex(CapuletEngine,NubbinBattery):
    def needs_service(self):
            if battery_should_be_serviced() or self.engine_should_be_serviced():
                return True
            else:
                return False
