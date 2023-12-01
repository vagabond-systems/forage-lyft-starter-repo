from .engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self):
        super().__init__(service_criteria=60000)
