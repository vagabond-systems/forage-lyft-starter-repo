from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, battery):
        self._battery = battery

    def needs_service(self):
        return (self.engine.needs_service() or self.battery.needs_service())


class Calliope(Car):
    def __init__(self, engine = None, battery = None):
        super().__init__(engine, battery)


class Glissade(Car):
    def __init__(self, engine = None, battery = None):
        super().__init__(engine, battery)


class Palindrome(Car):
    def __init__(self, engine = None, battery = None):
        super().__init__(engine, battery)


class Rorschach(Car):
    def __init__(self, engine = None, battery = None):
        super().__init__(engine, battery)


class Thovex(Car):
    def __init__(self, engine = None, battery = None):
        super().__init__(engine, battery)
