from tire.tire_interface import TireInterface


class OctoprimeTire(TireInterface):

    def needs_service(self):
        sum = 0
        for num in self.sensors:
            sum = sum + num

        if sum > 3:
            return True
        
        return False