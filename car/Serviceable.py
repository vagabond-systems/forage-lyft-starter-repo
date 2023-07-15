from abc import ABCMeta, abstractmethod


class Serviceable(metaclass=ABCMeta):
    
    @abstractmethod
    def needs_service():
        raise NotImplementedError
    
