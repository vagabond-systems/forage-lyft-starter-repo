from abc import abstractmethod


from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date


    @abstractmethod
    def needs_service(self):
        pass
