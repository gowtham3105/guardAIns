from ..Cell import Cell
from ..Guardian import Guardian
from ..Player import Player


class Gamora(Guardian):
    def __init__(self, belongs: Player, init_coordinates: Cell, alive=True):
        self.health = 125
        self.attack_damage = 50
        self.vision = 2
        self.speed = 2
        self.cooldown = 3
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # First check self.cooldown
        # then do whatever is required
        # JUMP anywhere within the radius
        return 0
