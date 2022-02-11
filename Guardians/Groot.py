from Cells.Cell import Cell
from Guardian import Guardian


# from Player import Player


class Groot(Guardian):
    def __init__(self, belongs, init_coordinates: Cell, alive=True):
        self.__health = 200
        self.attack_damage = 25
        self.vision = 2
        self.speed = 1
        self.cooldown = None
        super().__init__(belongs, init_coordinates, alive)

    def special_ability(self):
        # Call this in updation of each round
        # and increase health by 5
        return 0

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health
        if self.__health < 0:
            self.__health = 0
        elif self.__health > 200:
            self.__health = 200

        if self.__health <= 0:
            self.mark_as_dead()

        return self.__health

    def __repr__(self):
        return "Groot" + self.coordinates.__repr__()
