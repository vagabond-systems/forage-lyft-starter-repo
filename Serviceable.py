from abc import ABC, abstractmethod

class Serviceable():
    def __init__(self):
        print("self")
        
    @abstractmethod
    def need_service(self):
        pass