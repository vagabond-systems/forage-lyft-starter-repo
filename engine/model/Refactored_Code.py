from abc import ABC
from car import Car
from datetime import datetime

class Serviceable(self):
    def CarFactory(create_calliope, create_glissade, create_palindrome, create_rorschach, create_thovex):
        create_calliope(date current_date, date last_service_date, int current_mileage, int last_service_mileage)
        create_glissade(date current_date, date last_service_date, int current_mileage, int last_service_mileage)
        create_palindrome(date current_date, date last_service_date, bool warning_light_on)
        create_rorschach(date current_date, date last_service_date, int current_mileage, int last_service_mileage)
        create_thovex(date current_date, date last_service_date, int current_mileage, int last_service_mileage)