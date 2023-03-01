from .battery import Battery


class Nubbin(Battery):

  # Initating current date and last time battert was serviced
  def __init__(self, last_service_date, current_date):
    self.__last_service_date = last_service_date
    self.__current_date = current_date
    self.__number_of_years_to_be_serviced = 4

  # Overriding needs service method
  def needs_service(self):
    # Needs service once every 4 years
    if (self.__current_date - self.__last_service_date) > (self.__number_of_years_to_be_serviced * 365):
      return True
    return False
