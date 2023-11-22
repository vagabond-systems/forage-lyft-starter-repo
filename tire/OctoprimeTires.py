from serviceable import Serviceable


class OctoprimeTires:
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        """Check if Octoprime tires need service"""
        return sum(self.wear_array) >= 3
