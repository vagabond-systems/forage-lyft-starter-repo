from batteryStrategy import IBatteryStrategy


class BatteryContext:
    def __init__(self):
        self.strat = IBatteryStrategy

    def setStrategy(self, strategy):
        self.strat = strategy
