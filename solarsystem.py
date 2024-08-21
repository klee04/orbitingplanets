
import matplotlib.pyplot as plt
import math
import itertools

from vectors import Vector

class SolarSystem:
    def __init__(self, size)-> None:
        self.size = size
        self.bodies = []
        
        self.fig, self.ax = plt.subplots(1, 1, subplot_kw={"projection": "3d"}, figsize=(self.size / 50, self.size / 50))
        
        self.fig.tight_layout()
        self.ax.view_init(elev=0, azim=0)
        
    def add_body(self, body):
        self.bodies.append(body)
        
    def update_all(self):
        self.bodies.sort(key=lambda body: body.position[0])
        for body in self.bodies:
            body.move()
            body.draw()
            
    def draw_all(self):
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((-self.size/2, self.size/2))
        self.ax.set_zlim((-self.size/2, self.size/2))
        self.ax.axis(False)
        plt.pause(0.001)
        self.ax.clear()
        
    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for index, first in enumerate(bodies_copy):
            for second in bodies_copy[index+1:]:
                first.acceleration_due_to_gravity(second)
        

class SolarSystemBody:
    min_display_size = 10
    display_log_base = 1.3
    
    def __init__(self, solar_system: SolarSystem, mass: float, position: tuple=(0,0,0), velocity: Vector=(0,0,0))-> None:
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        
        self.display_size = max(math.log(self.mass, self.display_log_base), self.min_display_size)
        self.color = "black"
        
        self.solar_system.add_body(self)
        
    def move(self):
        x = self.position[0] + self.velocity[0]
        y = self.position[1] + self.velocity[1]
        z = self.position[2] + self.velocity[2]
        self.position = (x,y,z)
        
    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker = "o",
            markersize = self.display_size + self.position[0]/30,
            color = self.color
        )   
        
    def acceleration_due_to_gravity(self, other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_magnitude = distance.get_magnitude()
        
        force_magnitude = self.mass * other.mass / (distance_magnitude ** 2)
        force = distance.normalize() * force_magnitude
        
        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity  += acceleration * reverse
            reverse = -1
        
class Sun(SolarSystemBody):
    def __init__(self, solar_system, mass=10000, position=(0,0,0), velocity=(0,0,0)) -> None:
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.color = "yellow"


class Planet(SolarSystemBody):
    colors = itertools.cycle(["blue", "green", "red", "purple", "orange", "brown", "pink"])
    
    def __init__(self, solar_system, mass=10, position=(0,0,0), velocity=(0,0,0)) -> None:
        super(Planet, self).__init__(solar_system, mass, position, velocity)
        self.color = next(Planet.colors)