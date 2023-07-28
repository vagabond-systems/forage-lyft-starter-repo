from datetime import date
from car_factory import CarFactory

calliope = CarFactory.create_calliope(25000, 50000, date(2020, 1, 1), "Carrigan", [0.8, 0.9, 0.85, 0.95])
glissade = CarFactory.create_glissade(50000, 75000, date(2020, 1, 1), "Octoprime", [0.8, 0.9, 0.85, 0.95])
palindrome = CarFactory.create_palindrome(True, "Octoprime", [0.8, 0.9, 0.85, 0.95])
rorschach = CarFactory.create_rorschach(45000, 50000, date(2020, 1, 1), "Carrigan", [0.8, 0.9, 0.85, 0.95])
thovex = CarFactory.create_thovex(20000, 75000, date(2022, 1, 1), "Octoprime", [0.8, 0.9, 0.85, 0.95])

# Check if each car needs service
print("Calliope needs service:", calliope.needs_service())
print("Glissade needs service:", glissade.needs_service())
print("Palindrome needs service:", palindrome.needs_service())
print("Rorschach needs service:", rorschach.needs_service())
print("Thovex needs service:", thovex.needs_service())