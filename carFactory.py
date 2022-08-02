from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarFactory():
    def __init__(self):
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Calliope()

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Glissade()

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Palindrome()

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Rorschach()

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Thovex()