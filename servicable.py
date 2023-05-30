
from abc import ABC, abstractmethod


class Servicable(ABC):
    @abstractmethod
    def nees_service(self):
        pass