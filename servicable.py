from abc import ABC, abstractmethod


class Servicable(ABC):
    @abstractmethod
    def need_services(self):
        pass
