from battery import Battery

class SpindlerBatter(Battery):
    def __init__(self, current_date,last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        pass
