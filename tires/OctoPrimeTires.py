from tires.tires import Tires


class OctoPrimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_to_service = 3.0

    def need_service(self) -> bool:
        return sum(self.tire_wear) >= self.tire_need_to_service