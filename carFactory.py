from datetime import datetime

from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from car import Car


class CarFactory():

    def create_calliope(self, last_service_date, current_mileage, last_service_mileage):
        ce = CapuletEngine(last_service_mileage, current_mileage)
        sb = SpindlerBattery(last_service_date)
        self.car = Car(ce, sb)

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):
        we = WilloughbyEngine(last_service_mileage, current_mileage)
        sb = SpindlerBattery(last_service_date)
        self.car = Car(we, sb)

    def create_palindrome(self, last_service_date, warning_light_is_on):
        se = SternmanEngine(warning_light_is_on)
        sb = SpindlerBattery(last_service_date)
        self.car = Car(se, sb)

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):
        we = WilloughbyEngine(last_service_mileage, current_mileage)
        nb = NubbinBattery(last_service_date)
        self.car = Car(we, nb)

    def create_thovex(self, last_service_date, current_mileage, last_service_mileage):
        we = CapuletEngine(last_service_mileage, current_mileage)
        nb = NubbinBattery(last_service_date)
        self.car = Car(we, nb)

if __name__ == "__main__":

    today = datetime.today().date()
    cf = CarFactory()
    cf.create_calliope(today,30001,0)
    print(cf.car.needs_service())
