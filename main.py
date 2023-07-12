from car_factory import CarFactory
from datetime import datetime


car = CarFactory.create_calliope(datetime.today().date(),"2022-07-13",40000,20000)

print(car.needs_service())
