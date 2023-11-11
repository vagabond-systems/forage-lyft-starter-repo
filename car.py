from serviceable import Serviceable

# access cars via the Serviceable interface
class Car(Serviceable):
    def __init__(self, parts):
        # a car is a composition of different parts
        self.parts = parts

    def needs_service(self):
        # check each part to see if any of them need service
        for part in self.parts:
            if part.needs_service():
                return True

        return False
