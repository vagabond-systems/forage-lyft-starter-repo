from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Engine(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Battery(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 60000

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= 730  # 2 years

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= 1460  # 4 years

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

    from datetime import date

    class CarFactory:
        def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int,
                            last_service_mileage: int) -> Car:
            engine = CapuletEngine(last_service_mileage, current_mileage)
            battery = SpindlerBattery(last_service_date, current_date)
            return Car(engine, battery)

        def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int,
                            last_service_mileage: int) -> Car:
            engine = WilloughbyEngine(last_service_mileage, current_mileage)
            battery = SpindlerBattery(last_service_date, current_date)
            return Car(engine, battery)

        def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
            engine = SternmanEngine(warning_light_on)
            battery = SpindlerBattery(last_service_date, current_date)
            return Car(engine, battery)

        def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int,
                             last_service_mileage: int) -> Car:
            engine = WilloughbyEngine(last_service_mileage, current_mileage)
            battery = NubbinBattery(last_service_date, current_date)
            return Car(engine, battery)

        def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int,
                          last_service_mileage: int) -> Car:
            engine = CapuletEngine(last_service_mileage, current_mileage)
            battery = NubbinBattery(last_service_date, current_date)
            return Car(engine, battery)

