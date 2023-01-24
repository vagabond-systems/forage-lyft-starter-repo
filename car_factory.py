from .engines import (capulet, willoughby, sternman)
from .batteries import (nubbin, splinder)
from .car import Car

# Car Factory Class
class CarFactory:

  # Creating different types of cars
  def create_calliope(self, current_date, last_service_date, current_mileage,
                      last_service_mileage):
    return Car(splinder.Splinder(last_service_date, current_date),
               capulet.Capulet(last_service_mileage, current_mileage))

  def create_glissade(self, current_date, last_service_date, current_mileage,
                      last_service_mileage):
    return Car(splinder.Splinder(last_service_date, current_date),
               willoughby.Willoughby(last_service_mileage, current_mileage))

  def create_palindrome(self, current_date, last_service_date,
                        warning_lights_on):
    return Car(splinder.Splinder(last_service_date, current_date),
               sternman.Sternman(warning_lights_on))

  def create_rorschach(self, current_date, last_service_date, current_mileage,
                       last_service_mileage):
    return Car(nubbin.Nubbin(last_service_date, current_date),
               willoughby.Willoughby(last_service_mileage, current_mileage))

  def create_thovex(self, current_date, last_service_date, current_mileage,
                    last_service_mileage):
    return Car(nubbin.Nubbin(last_service_date, current_date),
               capulet.Capulet(last_service_mileage, current_mileage))
