from abc import ABC, abstractmethod

class Battery(ABC):
  # Creating needs service method
  @abstractmethod
  def needs_service(self):
    pass