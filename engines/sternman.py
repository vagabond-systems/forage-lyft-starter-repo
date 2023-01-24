from .engine import Engine


class Sternman(Engine):

  # Initating current status of warning light
  def __init__(self, warning_light_on):
    self.__warning_light_on = warning_light_on

  # Overriding needs service method
  def needs_service(self):
    # Needs service once warning light is on
    if (self.__warning_light_on):
      return True
    return False
