class SternmanEngine():
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self, val):
        self.warning_light_is_on = val
        return self.warning_light_is_on

    def perform_service(self):
        self.warning_light_is_on = False
