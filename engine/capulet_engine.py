from .engine import Engine

class CapuletEngine(Engine):
    def __init__(self):
        super().__init__(service_criteria=30000)
