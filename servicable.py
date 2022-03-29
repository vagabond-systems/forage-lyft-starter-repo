from abc import ABC, abstractmethod

class Servicable(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def needs_service(self)-> bool:
        pass