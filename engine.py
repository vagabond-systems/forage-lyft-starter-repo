from abc import abstractmethod

from car import Car


class Engine(Car):
    @abstractmethod
    def needs_service(self):
        pass