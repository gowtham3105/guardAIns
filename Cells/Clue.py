import random

from ..Cell import Cell

type_of_clue = ["enemy_seen", "node_Optimal_path"]


class Clue(Cell):
    def __init__(self):
        super().__init__()
        self.type = random.choice(type_of_clue)
        self.content = None

    def enemy_location():
        pass

    def get_best_node():
        pass
