from abc import ABC

class Tire(ABC):
    def __init__(self):
        pass

    def needs_service(self) -> bool:
        pass