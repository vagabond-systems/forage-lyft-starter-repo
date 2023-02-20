from abc import ABC


class Engine(ABC):
    def needs_service(self):
        pass