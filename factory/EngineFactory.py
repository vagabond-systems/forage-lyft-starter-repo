from engine.CapuletEngine import CapuletEngine
from engine.IEngine import IEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine


class EngineFactory:
    
    def create_engine(engine_type, last_service_mileage, current_mileage, warning_light_on) -> IEngine:
        
        if engine_type.Capitalize() == 'Sternman':
            return SternmanEngine(warning_light_on)
        elif engine_type.Capitalize() == 'Capulet':
            return CapuletEngine(last_service_mileage, current_mileage)
        elif engine_type.Capitalize() == 'Willoughby':
            return WilloughbyEngine(last_service_mileage, current_mileage)
        else:
            raise ValueError('Wrong engine inputted')
    
    