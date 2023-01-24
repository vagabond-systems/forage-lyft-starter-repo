from .serviceable import Serviceable 
"""
Base class for cars
"""


class Car(Serviceable):
  # Initiate attributes using composition
  def __init__(self, battery, engine):
    self._battery = battery
    self._engine = engine

  # Overriding the needs_service method
  def needs_service(self):
    if self._battery.needs_service() or self._engine.needs_service():
      return True
    return False
  