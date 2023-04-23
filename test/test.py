from carFactory import CarFactory
from datetime import date, datetime

carfactory = CarFactory()
current_date = date.today()
last_service_date = datetime(2022, 1, 1).date()
car = carfactory.create_palindrome(current_date, last_service_date, False)
car2 = carfactory.create_glissade(current_date, last_service_date, 168123, 102312 )

print(car.needs_service())
print(car2.needs_service())