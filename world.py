import random
import math

class World:
    def __init__(self, size, difficulty):
        self.size = size
        self.difficulty = difficulty
        self.base_position = (0,0)

        self.energy_zones = self.generate_points(6)
        self.danger_zones = self.generate_points(8)
        self.repair_stations = self.generate_points(4)
        self.core_position = random.choice(self.generate_points(10))

    
    def generate_points(self, amount):
        points = []

        for _ in range(amount):
            x = random.randint(-self.size + 10,self.size - 10)
            y = random.randint(-self.size + 10, self.size - 10)
            points.append((x,y))
        
        return points
    
    def distance_to_base(self, x, y):
        return int(math.dist((x,y), self.base_position))
