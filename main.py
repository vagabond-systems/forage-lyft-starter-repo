from datetime import datetime
from car_factory import MyCarFactory


def main():
    my_car_factory = MyCarFactory()

    calliope = my_car_factory.create_car("Calliope", last_service_date = datetime(2024, 6, 1), current_mileage=25000, last_service_mileage=20000)
    glissade = my_car_factory.create_car("Glissade", last_service_date = datetime(2010, 3, 15), current_mileage=55000, last_service_mileage=50000)
    palindrome = my_car_factory.create_car("Palindrome", last_service_date = datetime(2022, 9, 20), warning_light_on=True)
    rorschach = my_car_factory.create_car("Rorschach", last_service_date = datetime(2020, 2, 10), current_mileage=70000, last_service_mileage=60000) 
    thovex = my_car_factory.create_car("Thovex", last_service_date = datetime(2021, 7, 5), service_interval=4)

    cars = [calliope, glissade, palindrome, rorschach, thovex]
    for car in cars:
        if car.needs_service():
            print(f"{car.__class__.__name__} needs service")
        else:
            print(f"{car.__class__.__name__} doesn't need service")
    
if __name__ == "__main__":
    main()
