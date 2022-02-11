from Cells.Cell import Cell
from Guardian import Guardian


# from Player import Player


class StarLord(Guardian):
    def __init__(self, belongs, init_coordinates: Cell, alive=True):
        self.__health = 100
        self.attack_damage = 35
        self.vision = 5
        self.speed = 2
        self.cooldown = None
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # See Through Walls, upto range one,
        # i.e one block behind a wall can be seen
        return 0

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health
        if self.__health < 0:
            self.__health = 0
        elif self.__health > 100:
            self.__health = 100

        if self.__health <= 0:
            self.mark_as_dead()

        return self.__health

    def __repr__(self):
        return "StarLord" + self.coordinates.__repr__()
