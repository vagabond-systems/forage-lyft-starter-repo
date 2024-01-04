from abc import ABC

class Car():
    def __init__(self, battery, engine, car_type):
        self.battery = battery
        self.engine = engine
        self.car_type = car_type
        car_type = []**5

    def create_car(self, battery, engine, car_type):
        car_type = [calliope['',''], glissade['',''], palindrome['',''], rorschach['',''], thovex['','']]
        if battery == 'spindler' and engine == 'capulet':
             calliope = ['spindler', 'capulet']
             car_type[calliope] = calliope

        elif battery ==  'spindler' and engine == 'willoughby':
            glissade = Car('spindler', 'wiloughby')
            car_type[glissade] = glissade
            
        elif battery ==  'spindler' and engine == 'sternman':
            palindrome = Car('spindler', 'sternman')
            car_type[palindrome] = palindrome

        elif battery ==  'nubbin' and engine == 'willoughby':
            rorschach = Car('nubbin', 'willoughby')
            car_type[rorschach] = rorschach

        elif battery ==  'nubbin' and engine == 'capulet':
            thovex = Car('nubbin', 'capulet')
            car_type[thovex] = thovex

        return car_type





    

        
