from abc import ABC, abstractmethod


class CarFactory(ABC):
    @abstractmethod
    def create_car(self, car_type, **kwargs):
        pass
