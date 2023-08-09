from datetime import date
from CarFactory import CarFactory

calliope = CarFactory.create_calliope( date(2017, 2, 3), date(2020, 1, 1), 25000, 50000, [0.1, 0.3, 0.2, 0.1])
glissade = CarFactory.create_glissade(  date(2019, 1, 1), date(2020, 1, 1), 50000, 75000, [0.1, 0.4, 0.85, 0.95])
palindrome = CarFactory.create_palindrome(date(2020, 1, 1), date(2020, 1, 1), True, [0.8, 0.9, 0.85, 0.95])
rorschach = CarFactory.create_rorschach(date(2020, 1, 1), date(2020, 1, 1), 45000, 50000,  [0.8, 0.9, 0.85, 0.95])
thovex = CarFactory.create_thovex( date(2020, 1, 1), date(2022, 1, 1), 20000, 75000, [0.8, 0.9, 0.85, 0.95])

print("Calliope needs service:", calliope.needs_service())
print("Glissade needs service:", glissade.needs_service())
print("Palindrome needs service:", palindrome.needs_service())
print("Rorschach needs service:", rorschach.needs_service())
print("Thovex needs service:", thovex.needs_service())