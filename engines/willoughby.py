from .engine import Engine


class Willoughby(Engine):

  # Initating current milage vs last time sercicw
  def __init__(self, last_service_milage, current_milage):
    self.__last_service_milage = last_service_milage
    self.__current_milage = current_milage
    self.__service_milage = 60000

  # Overriding needs service method
  def needs_service(self):
    # Needs service once warning light is on
    if (self.__current_milage -
        self.__last_service_milage) > self.__service_milage:
      return True
    return False
