# from Cells.Cell import Cell
# from Player import Player
from Feedback import Feedback

class Guardian:

    def __init__(self, belongs, init_coordinates, alive=True):
        self.belongs_to_player = belongs
        self.coordinates = init_coordinates
        self.__is_alive = alive

    def attack(self, cell):
        # check if cell has an enemy i.e guardian from opposite team
        # update health
        return 0

    def update_cooldown(self):
        # called from environment, cold own is updated after every round
        return 0

    def mark_as_dead(self, alive=False):
        # marks a player as dead
        self.__is_alive = False
        return Feedback("guardian_died", {"coordinates": self.coordinates})

    def is_alive(self):
        return self.__is_alive

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def get_belongs_to_player(self):
        return self.belongs_to_player
