from Cell import Cell
from Guardian import Guardian


# from Player import Player


class StarLord(Guardian):
    def __init__(self, belongs, init_coordinates: Cell, alive=True):
        self.health = 100
        self.attack_damage = 35
        self.vision = 5
        self.speed = 2
        self.cooldown = None
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # See Through Walls, upto range one,
        # i.e one block behind a wall can be seen
        return 0
