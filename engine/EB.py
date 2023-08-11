from abc import ABC, abstractmethod


class Engine():
    @abstractmethod
    def needs_service(self):
        pass
    


class Battery():
    @abstractmethod
    def needs_service(self):
       pass