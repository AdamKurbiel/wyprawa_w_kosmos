import math

class Spaceship:
    def __init__(
            self,
            expedition_name,
            name,
            x,
            y,
            angle,
            energy,
    ):
        self.expedition_name = expedition_name
        self.name = name
        self.x = x
        self.y = y
        self.angle = angle
        self.energy = energy

        self.integrity = 100
        self.steps = 0
        self.found_core = False
    
    def move(self, world, turbo=False):
        speed = 12 if turbo else 6

        cost = 12 if turbo else 5

        radians = math.radians(self.angle)

        new_x = round(self.x + math.cos(radians) * speed)
        new_y = round(self.y + math.sin(radians) * speed)

        if not world.inside_world(new_x, new_y):
            self.energy -= 8
            return "Statek odbił się od granicy świata i stracił energię."
        
        self.x = new_x
        self.y = new_y

        self.energy -= cost

        if turbo:
            self.integrity -= 5
            return "Aktywowano tryb turbo."
        
        return "Statek przemieścił się do przodu."
    
    def turn(self,amount):
        self.angle = (self.angle + amount) % 360
    
    def calculate_score(self, status):
        score = self.energy + self.integrity

        if self.found_core:
            score += 100

        if status == "SUKCES":
            score += 200
        
        score -= self.steps * 2

        return max(score, 0)