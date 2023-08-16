from datetime import datetime

class CarriganTire:
    def __init__(self,sensor_response_array: list) -> None:
        self.__sensor_response_array = sensor_response_array
    def needs_service(self) -> bool:
        for response in self.__sensor_response_array:
            if response >= 0.9:
                return True
        return False