from abc import ABC, abstractmethod


class Engine(ABC):
  # Creating needs service method
  @abstractmethod
  def needs_service(self):
    pass
