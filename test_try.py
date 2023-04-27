from carFactory import CarFactory
from datetime import datetime


class Test:
    def __init__(self):
        self.carfactory = CarFactory()

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        calliope = self.carfactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage)
        print(calliope.needs_service())


test = Test()
test.test_battery_should_be_serviced()
