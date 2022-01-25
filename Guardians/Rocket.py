from ..Cell import Cell
from ..Guardian import Guardian
from ..Player import Player


class Rocket(Guardian):
    def __init__(self, belongs: Player, init_coordinates: Cell, alive=True):
        self.health = 75
        self.attack_damage = 35
        self.vision = 4
        self.speed = 3
        self.cooldown = None
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # Definite Attack, Lockon Attack
        return 0
