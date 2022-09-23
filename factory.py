import car
import engine
import battery

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = car.Calliope()
        calliope.engine = engine.CapuletEngine(current_mileage, last_service_mileage)
        calliope.battery = battery.SpindlerBattery(current_date, last_service_date)
        return calliope

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = car.Glissade()
        glissade.engine = engine.WilloughbyEngine(current_mileage, last_service_mileage)
        glissade.battery = battery.SpindlerBattery(current_date, last_service_date)
        return glissade

    def create_palindrome(self, current_date, last_service_date):
        palindrome = car.Palindrome()
        palindrome.engine = engine.SternmanEngine()
        palindrome.battery = battery.SpindlerBattery(current_date, last_service_date)
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = car.Rorschach()
        rorschach.engine = engine.WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach.battery = battery.NubinBattery(current_date, last_service_date)
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = car.Thovex()
        thovex.engine = engine.CapuletEngine(current_mileage, last_service_mileage)
        thovex.battery = battery.NubinBattery(current_date, last_service_date)
        return thovex

    
# f = CarFactory()
# c = f.create_glissade("2020-09-23", "2019-09-23", 140000, 80000) ## 60k / 2yr
# print(c.needs_service())

# print(" ")

# c = f.create_palindrome("2020-09-23", "2019-09-23") ## indicator / 2yr 
# print(c.needs_service())

# print(" ")

# c = f.create_rorschach("2020-09-23", "2019-09-23", 100000, 80000)## 60k / 4yr
# print(c.needs_service())

# print(" ")

# c = f.create_thovex("2020-09-23", "2019-09-23", 110000, 80000) ## 30k / 4yr 
# print(c.needs_service())