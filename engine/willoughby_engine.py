from engine.engine import Engine


# class variables are private
class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    # serviced every 60k miles
    def needs_service(self) -> bool:
        return self.__current_mileage - self.__last_service_mileage > 60000
