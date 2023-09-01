class Tire:
    name = ""
    service_criteria = None

    def __init__(self, name):
        self.name = name

    def needs_service(self, tire_wear_array):
        return self.service_criteria(tire_wear_array)
    def service_criteria(tire_wear_array):
        return any(tire_wear >= 0.9 for tire_wear in tire_wear_array)
    def service_criteria(tire_wear_array):
        return sum(tire_wear_array) >= 3

