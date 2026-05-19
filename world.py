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
    
    def distance_to_core(self, x, y):
        return int(math.dist((x,y), self.core_position))
    
    def inside_world(self, x, y):
        return -self.size <= x <= self.size and -self.size <= y <= self.size
    
    def apply_world_effect(self, vehicle):
        position = (vehicle.x, vehicle.y)

        if position == self.core_position and not vehicle.found_core:
            vehicle.found_core = True
            vehicle.energy += 30
            return "Odnaleziono rdzeń energetyczny."
        
        if position in self.energy_zones:
            vehicle.energy += 20
            return "Aktywna strefa energii zwiększyła poziom zasilania."
        
        if position in self.danger_zones:
            vehicle.integrity -= 20
            return "Statek wleciał w niebezpieczną anomalię."
        
        if position in self.repair_stations:
            vehicle.integrity += 15
            vehicle.integrity = min(vehicle.integrity, 100)
            return "Automatyczna stacja naprawcza przywróciła integralność."
        
        return None
    
    def scan_area(self,x,y):
        distance = self.distance_to_core(x,y)

        if distance < 15:
            return "Skaner wykrywa silne źródło energii bardzo blisko."
        
        if distance < 35:
            return "Skaner wykrywa niestabilne impulsy energetyczne."
        
        return "Brak istotnych sygnałów w pobliżu."