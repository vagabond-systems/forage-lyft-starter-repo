from datetime import datetime

from engine.Capulet_And_Willoughby_engine import Capulet_And_Willoughby_engine


class Glissade_And_Calliope(Capulet_And_Willoughby_engine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
