from Cells.Cell import Cell
from Cells.Clue import Clue
from Feedback import Feedback
from Player import Player


class Beast(Clue):
    def __init__(self, cell: Cell):
        super().__init__(cell, Cell.Beast)
        self.__is_alive = True

    def update_health(self,
                      player: Player):  # call this in update rounds every round for each player and it returns the clue if available
        if self.__is_alive:
            if len(self.__rounds_left) > 0:
                self.__rounds_left -= 1
            guardian = self.get_guardians_present()[0]
            if guardian.belongs_to_player == player:
                reduce_health = guardian.set_health(guardian.get_health() - self.__damage)
                if reduce_health != None:
                    return reduce_health
                else:
                    clue = Feedback("clue", self.get_clue())
                    return clue
