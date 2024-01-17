from engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_status:bool):
        self.warning_light_status = warning_light_status

    def needs_service(self) -> bool:
        return self.warning_light_status
