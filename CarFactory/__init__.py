from datetime import datetime
from Car.__init__ import Car

from Engine.capulet_engine import CapuletEngine
from Engine.sternman_engine import SternmanEngine
from Engine.willoughby_engine import WilloughbyEngine

from Battery.nubbin_battery import NubbinBattery
from Battery.spindler_battery import SpindlerBattery


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date, last_service_date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        return Car(
            engine=CapuletEngine(
                last_service_date, current_mileage, last_service_mileage
            ),
            battery=SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_glissade(
        current_date, last_service_date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        return Car(
            engine=WilloughbyEngine(
                last_service_date, current_mileage, last_service_mileage
            ),
            battery=SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_palindrome(
        current_date, last_service_date, warning_light_on: bool
    ) -> Car:
        return Car(
            engine=SternmanEngine(last_service_date, warning_light_on),
            battery=SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_rorschach(
        current_date, last_service_date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        return Car(
            engine=WilloughbyEngine(
                last_service_date, current_mileage, last_service_mileage
            ),
            battery=NubbinBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_thovex(
        current_date, last_service_date, current_mileage: int, last_service_mileage: int
    ) -> Car:
        return Car(
            engine=CapuletEngine(
                last_service_date, current_mileage, last_service_mileage
            ),
            battery=NubbinBattery(last_service_date, current_date),
        )


# example:
current_date = datetime.today()
last_service_date = datetime(2022, 7, 1)
current_mileage = 50000
last_service_mileage = 48000

calliope_car = CarFactory.create_calliope(
    current_date, last_service_date, current_mileage, last_service_mileage
)
glissade_car = CarFactory.create_glissade(
    current_date, last_service_date, current_mileage, last_service_mileage
)
palindrome_car = CarFactory.create_palindrome(current_date, last_service_date, True)
rorschach_car = CarFactory.create_rorschach(
    current_date, last_service_date, current_mileage, last_service_mileage
)
thovex_car = CarFactory.create_thovex(
    current_date, last_service_date, current_mileage, last_service_mileage
)
