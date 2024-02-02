from abc import ABC


class Battery(ABC):
    # Doesn't need constructor

    def needs_service(self):
        pass