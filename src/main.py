from model.calliope import Calliope
from datetime import date


c = Calliope(date(2019, 12, 5), 60000, 500)

print(c.needs_service())
