from abc import ABC

class Battery(ABC):
    def needs_service(self)-> bool:
        pass

    # question: as it only takes one parameter, will it not throw an error when we pass more than one parameters?