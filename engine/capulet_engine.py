from engine.engine import Engine


class CapuletEngine(Engine):

    # private class variables for the engine
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    # serviced every 30k miles
    def engine_should_be_serviced(self) -> bool:
        return (self.__current_mileage - self.__last_service_mileage) > 30000
