from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
<<<<<<< HEAD
        return self.engine.needs_service() or self.battery.needs_service()
=======
        return self.engine.needs_service() or self.battery.needs_service()
>>>>>>> b0e04759e21b1dd9fa81846dda078a2cfb447fb5
