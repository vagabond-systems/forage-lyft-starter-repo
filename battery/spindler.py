import battery as Battery


class Spindler(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
    
    def needs_service(self):
        return self.current_date - self.last_service_date > 2