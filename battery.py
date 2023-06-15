class Battery:
    def __init__(self, type):
        self.type = type

    def getType(self):
        return self.type

    def needsService(self, years):
        # Logic to determine if the battery needs service based on years
        pass

class Spindler(Battery):
    def needs_service(self, years: int) -> bool:
        return years >= 3  # Updated service criteria to 3 years
