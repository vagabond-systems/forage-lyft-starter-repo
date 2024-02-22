from datetime import date

class Serviceable:
    def needs_service(self) -> bool:
        pass

class Engine(Serviceable):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        # Logic to determine if engine needs service
        pass

class Battery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        # Logic to determine if battery needs service
        pass

class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class NubbinBattery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        # Logic to determine if NubbinBattery needs service
        pass

class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        # Logic to determine if SpindlerBattery needs service
        pass

class SternmanEngine(Serviceable):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on
    
    def needs_service(self) -> bool:
        # Logic to determine if SternmanEngine needs service
        pass

class WilloughbyEngine(Serviceable):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        # Logic to determine if WilloughbyEngine needs service
        pass

class CapuletEngine(Serviceable):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        # Logic to determine if CapuletEngine needs service
        pass

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
