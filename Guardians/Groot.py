from ..Cell import Cell
from ..Guardian import Guardian
from ..Player import Player


class Groot(Guardian):
    def __init__(self, belongs: Player, init_coordinates: Cell, alive=True):
        self.health = 200
        self.attack_damage = 25
        self.vision = 2
        self.speed = 1
        self.cooldown = None
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # Call this in updation of each round
        # and increase health by 5
        return 0
