from engine.willoughby_engine import WilloughbyEngine
from utils import needs_service


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        return needs_service(self)
