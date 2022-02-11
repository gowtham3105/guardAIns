from Cells.Cell import Cell
from Guardian import Guardian


# from Player import Player


class Drax(Guardian):
    def __init__(self, belongs, init_coordinates: Cell, alive=True):
        self.__health = 150
        self.attack_damage = 70
        self.vision = 1
        self.speed = 1
        self.cooldown = 3
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # See Through Walls, upto range one,
        # behind a wall can be seen
        return 0

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health
        if self.__health < 0:
            self.__health = 0
        elif self.__health > 150:
            self.__health = 150

        if self.__health <= 0:
            self.mark_as_dead()

    def __repr__(self):
        return "Drax" + self.coordinates.__repr__()
