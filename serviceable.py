from abc import ABC, abstractmethod
"""
Interface for serviceable
"""

class Serviceable(ABC):

  # Abstract method for checking if the car needs service
  @abstractmethod
  def needs_service(self):
    pass