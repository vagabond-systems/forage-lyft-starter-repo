from tire.tire_interface import TireInterface


class CarriganTire(TireInterface):

    def needs_service(self):
        for num in self.sensors:
            if num >= 0.9:
                return True

        return False    
