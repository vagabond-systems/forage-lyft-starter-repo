import abc as ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass