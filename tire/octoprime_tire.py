from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self,sensor_response_array: list) -> None:
        self.__sensor_response_array = sensor_response_array
    def needs_service(self) -> bool:
        if sum(self.__sensor_response_array) >= 3:
            return True
        return False