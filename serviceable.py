import abc as ABC, abstractmethod


class serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass