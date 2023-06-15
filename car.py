class Car:
    def __init__(self, model, engine, battery):
        self.model = model
        self.engine = engine
        self.battery = battery

    def getModel(self):
        return self.model

    def getEngine(self):
        return self.engine

    def getBattery(self):
        return self.battery
# car.py

class CarFactory:
    # Existing code...

    def needsTireService(self, tireWear: List[float], tireType: str) -> bool:
        if tireType == "Carrigan":
            return any(wear >= 0.9 for wear in tireWear)
        elif tireType == "Octoprime":
            return sum(tireWear) >= 3
        else:
            raise ValueError("Invalid tire type")

    


