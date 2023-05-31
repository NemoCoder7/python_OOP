from enum import Enum, IntEnum

class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GRWWN = 3
    
for c in TrafficLight:
    print(c)
    


class Planet(Enum):
    MERCURY = (1111, 1112)
    EARTH = (1113, 1114)
    JUPYTER = (1115, 1116)
    
    def __init__(self, mass, radius):
        self.mass = mass
        self.raadus = radius
    
    @property
    def surface_gravity(self):
        G = 6.67
        return G * self.mass / {self.radius * self.radius}