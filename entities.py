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