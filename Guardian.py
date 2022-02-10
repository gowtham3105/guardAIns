# from Cells.Cell import Cell
# from Player import Player


class Guardian:

    def __init__(self, belongs, init_coordinates, alive=True):
        self.belongs_to_player = belongs
        self.coordinates = init_coordinates
        self.is_alive = alive

    def attack(self, cell):
        # check if cell has an enemy i.e guardian from opposite team
        # update health
        return 0

    def update_cooldown(self):
        # called from environment, cold own is updated after every round
        return 0

    def mark_as_dead(self, alive=False):
        # marks a player as dead
        self.is_alive = False

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates
