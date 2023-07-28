from abc import ABC

class Battery(ABC):
    def __init__(self):
        pass

    def needs_service(self) -> bool:
        pass