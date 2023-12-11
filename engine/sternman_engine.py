from .engine import Engine

class SternmanEngine(Engine):
    def __init__(self):
        super().__init__(service_criteria=float('inf'))
