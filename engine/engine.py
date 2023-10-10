from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass