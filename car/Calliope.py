from car.Car import Car

class Calliope(Car):
    
    def __init__(self,  engine, battery, last_service_date):
        super().__init__(last_service_date)
        super().set_battery(battery)
        super().set_engine(engine)
    
        
    