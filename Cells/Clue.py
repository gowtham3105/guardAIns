import random

from Cells.Cell import Cell

type_of_clue = ["enemy_seen", "node_Optimal_path"]


class Clue(Cell):
    def __init__(self):
        super().__init__()
        self.__cell_type = "Clue"
        self.type = random.choice(type_of_clue)
        self.content = None

    def enemy_location(self):
        pass

    def get_best_node(self):
        pass
