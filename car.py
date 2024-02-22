from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

# Import necessary modules
from datetime import datetime

# Define the Car class representing a car with Spindler batteries
class Car:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        # Spindler battery requires service after three years
        current_date = datetime.now()
        service_interval = 3  # Service interval for Spindler batteries (in years)
        if (current_date.year - self.last_service_date.year) >= service_interval:
            return True
        else:
            return False

# Define the CarriganCar class representing a car with Carrigan tires
class CarriganCar:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        # Carrigan tires should be serviced if one or more tire wear values are >= 0.9
        if self.tire_wear and max(self.tire_wear) >= 0.9:
            return True
        else:
            return False

# Define the OctoprimeCar class representing a car with Octoprime tires
class OctoprimeCar:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        # Octoprime tires should be serviced if sum of tire wear values is >= 3
        if self.tire_wear and sum(self.tire_wear) >= 3:
            return True
        else:
            return False

