from model.car_factory import CarFactory
from datetime import date


c = CarFactory.create_rorschach(date(2019, 12, 5), 60000, 500)

print(c.needs_service())
