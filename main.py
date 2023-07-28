from datetime import date
from car_factory import CarFactory

calliope = CarFactory.create_calliope(25000, date(2020, 1, 1))
glissade = CarFactory.create_glissade(50000, date(2020, 1, 1))
palindrome = CarFactory.create_palindrome(True)
rorschach = CarFactory.create_rorschach(45000, date(2020, 1, 1))
thovex = CarFactory.create_thovex(20000, date(2022, 1, 1), )

# Check if each car needs service
print("Calliope needs service:", calliope.needs_service())
print("Glissade needs service:", glissade.needs_service())
print("Palindrome needs service:", palindrome.needs_service())
print("Rorschach needs service:", rorschach.needs_service())
print("Thovex needs service:", thovex.needs_service())