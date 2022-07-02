from engine.engine import Engine


# serviced every 30k miles
class CapuletEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    # returns true if driven more than 30k miles since last service
    def needs_service(self) -> bool:
        return (self.__current_mileage - self.__last_service_mileage) > 30000
