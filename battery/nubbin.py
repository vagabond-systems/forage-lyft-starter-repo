import battery as Battery


class Nubbin(Battery):
    def __init__(self):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        return this.current_date - this.last_service_date > 4