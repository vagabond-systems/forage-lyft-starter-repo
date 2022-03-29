import datetime
from engine.model import calliope, glissade, palindrome,rorschach, thovex


class CarFactory:
    def __init__(self, last_service_date, current_mileage, last_service_mileage, warning_light_on=False):
        
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        return calliope.Calliope(last_service_date=self.last_service_date, current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage)


    def create_glissade(self):
        return glissade.Glissade(last_service_date=self.last_service_date, current_mileage=self.current_mileage, last_service_mileage=self.last_service_date)

    def create_palindrome(self):
        return palindrome.Palindrome(last_service_date=self.last_service_date, current_mileage=self.current_mileage, last_service_mileage=self.last_service_date, warning_light_on=self.warning_light_on)

    def create_rorschach(self):
        return rorschach.Rorschach(last_service_date=self.last_service_date, current_mileage=self.current_mileage, last_service_mileage=self.last_service_date)

    def create_thovex(self):
        return thovex.Thovex(last_service_date=self.last_service_date, current_mileage=self.current_mileage, last_service_mileage=self.last_service_date)