from abc import ABC
from datetime import datetime

class Engine(ABC):

    def needs_service(self):
        pass