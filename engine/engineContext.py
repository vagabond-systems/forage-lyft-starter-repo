from engineStrategy import IEngineStrategy


class EngineContext:
    def __init__(self):
        self.strat = IEngineStrategy

    def setStrategy(self, strategy):
        self.strat = strategy