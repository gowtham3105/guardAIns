import random

from Cells.Cell import Cell
from InfinityStone import InfinityStone
from Player import Player

type_of_clue = ["enemy_seen", "node_Optimal_path"]


class Clue(Cell):
    def __init__(self, cell: Cell, cell_type=None):
        if not cell_type:
            super().__init__(cell.get_coordinates(), cell.get_guardians_present(), cell.get_neighbour_cells(),
                             Cell.Clue)
        else:
            super().__init__(cell.get_coordinates(), cell.get_guardians_present(), cell.get_neighbour_cells(),
                             cell_type)
        self.type = random.choice(type_of_clue)  # equal probability
        self.is_clue_active = False

    def enemy_location(self, opponentPlayer: Player):
        return_dict = {}
        for troop_name, troop in opponentPlayer.guardians().items():
            if troop.is_alive:
                return_dict[troop_name] = str(troop.get_coordinates())
        return {"enemy_locations": return_dict}

    def get_best_direction(self, infinityStone: InfinityStone):
        direcionSlope = (self.get_coordinates()[1]-infinityStone.get_coordinates()[1])/(self.get_coordinates()[0]-infinityStone.get_coordinates()[0]) # TODO: check order
        return {"infinity_stone_direction":direcionSlope}
    def get_clue(self,opponentPlayer:Player,infinityStone:InfinityStone, player:Player):
        if self.is_clue_active:
            if self.type == "enemy_seen":
                return self.enemy_location()
            elif self.type == "node_Optimal_path":
                return self.get_best_direction()
        else:
            return
