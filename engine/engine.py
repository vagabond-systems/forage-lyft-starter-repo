from abc import ABCMeta

class Engine(ABC):
    def needs_service(self):
        pass