from engine.capulet_engine import CapuletEngine
from utils import needs_service


class Calliope(CapuletEngine):
    def needs_service(self):
        return needs_service(self)
