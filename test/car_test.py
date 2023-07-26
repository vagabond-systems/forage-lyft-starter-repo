import unittest
from datetime import date, datetime
from battery.NubbinBattery import NubbinBattery
from battery.SplinderBattery import SplinderBattery


from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
from tires.CarriganTires import CarriganTires
from tires.OctoPrimeTires import OctoPrimeTires


class test_capuletengine(unittest.TestCase):
    def engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001
        
        self.asserTrue(CapuletEngine.need_service())
    
    def engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30000
        
        self.assertFalse(CapuletEngine.need_service())
        

class test_sternmanengine(unittest.TestCase):
    def engine_should_be_serviced(self):
        warning_light_on = True
        
        self.assertTrue(SternmanEngine.need_service())
    
    def engine_should_not_be_serviced(self):
        warning_light_on = False
        
        self.assertFalse(SternmanEngine.need_service())
        

class test_willoughbyengine(unittest.TestCase):
    def engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60001
        
        self.assertTrue(WilloughbyEngine.need_service())
        
    def engine_should_not_be_replaced(self):
        last_service_mileage = 0
        current_mileage = 60000
        
        self.assertFalse(WilloughbyEngine.need_service())
    
class test_nubbinbattery(unittest.TestCase):
    def battery_should_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        
        self.assertTrue(NubbinBattery.need_service())
    
    def battery_should_not_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        
        self.assertFalse(NubbinBattery.need_service())
        

class test_splinderbattery(unittest.TestCase):
    def battery_should_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4)
        
        self.assertTrue(SplinderBattery.need_service())
    
    def battery_should_not_be_replaced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 2)
        
        self.assertFalse(SplinderBattery.need_service())
        
class test_carrigantires(unittest.TestCase):
    def tire_needs_service(self):
        tire_wear = [0.9,0.1,0.8,0.2]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.need_service())
    
    def tire_notneeds_service(self):
        tire_wear = [0.2,0.1,0.3,0.4]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.need_service())


class test_octoprimetires(unittest.TestCase):
    def tire_needs_service(self):
        tire_wear = [0.9,0.9,0.9,0.4]
        tires = OctoPrimeTires(tire_wear)
        self.assertTrue(tires.need_service())
    
    def tire_notneeds_service(self):
        tire_wear = [0.2,0.1,0.3,0.4]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.need_service())
    
           

if __name__ == '__main__':
    unittest.main()
    