from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from engine.engineStrategy import IEngineStrategy
from battery.batteryStrategy import IBatteryStrategy
from tire.tireStrategy import ITireStrategy


class CarFactory():
    def __init__(self):
        self.car = Car(engineStrategy=IEngineStrategy,
                       batterySrategy=IBatteryStrategy, tireStrategy=ITireStrategy)

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tires, tire_values):
        self.car.engineStrategy = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        if tires == 'Carrigan':
            self.car.tireStrategy = CarriganTire(tire_values)
        elif tires == 'Octoprime':
            self.car.tireStrategy = OctoprimeTire(tire_values)
        else:
            raise ValueError(
                f"Expected Carrigan or Octoprime, recieved {tires} instead")
        return self.car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tires, tire_values):
        self.car.engineStrategy = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        if tires == 'Carrigan':
            self.car.tireStrategy = CarriganTire(tire_values)
        elif tires == 'Octoprime':
            self.car.tireStrategy = OctoprimeTire(tire_values)
        else:
            raise ValueError(
                f"Expected Carrigan or Octoprime, recieved {tires} instead")
        return self.car

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tires, tire_values):
        self.car.engineStrategy = SternmanEngine(
            warning_light_is_on=warning_light_on)
        self.car.batteryStrategy = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        if tires == 'Carrigan':
            self.car.tireStrategy = CarriganTire(tire_values)
        elif tires == 'Octoprime':
            self.car.tireStrategy = OctoprimeTire(tire_values)
        else:
            raise ValueError(
                f"Expected Carrigan or Octoprime, recieved {tires} instead")
        return self.car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tires, tire_values):
        self.car.engineStrategy = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        if tires == 'Carrigan':
            self.car.tireStrategy = CarriganTire(tire_values)
        elif tires == 'Octoprime':
            self.car.tireStrategy = OctoprimeTire(tire_values)
        else:
            raise ValueError(
                f"Expected Carrigan or Octoprime, recieved {tires} instead")
        return self.car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tires, tire_values):
        self.car.engineStrategy = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        if tires == 'Carrigan':
            self.car.tireStrategy = CarriganTire(tire_values)
        elif tires == 'Octoprime':
            self.car.tireStrategy = OctoprimeTire(tire_values)
        else:
            raise ValueError(
                f"Expected Carrigan or Octoprime, recieved {tires} instead")
        return self.car
