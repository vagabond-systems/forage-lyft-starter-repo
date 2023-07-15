from car.Car import Car

class Thovex(Car):
    
    def __init__(self,  engine, battery, current_date, last_service_date, 
                 last_service_mileage, current_mileage):
        super().__init__(current_date, last_service_date, last_service_mileage, current_mileage)
        super().set_battery(battery)
        super().set_engine(engine)
    
    
