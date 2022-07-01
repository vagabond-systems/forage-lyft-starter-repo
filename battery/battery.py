from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def battery_should_be_serviced(self):
        pass
