from abc import ABC, abstractmethod
from typing import List


class Tire(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass