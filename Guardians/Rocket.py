from Cells.Cell import Cell
from Guardian import Guardian


# from Player import Player


class Rocket(Guardian):
    def __init__(self, belongs, init_coordinates: Cell, alive=True):
        self.__health = 75
        self.attack_damage = 35
        self.vision = 4
        self.speed = 3
        self.cooldown = None
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # Definite Attack, Lockon Attack
        return 0

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health
        if self.__health < 0:
            self.__health = 0
        elif self.__health > 75:
            self.__health = 75

        if self.__health <= 0:
            self.mark_as_dead()

        return self.__health

    def __repr__(self):
        return "Rocket" + self.coordinates.__repr__()
