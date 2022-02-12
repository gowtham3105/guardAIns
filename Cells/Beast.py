from functools import reduce
from Feedback import Feedback
from Player import Player
from .Clue import Clue
from InfinityStone import InfinityStone

class Beast(Clue):
    def __init__(self,player1:Player,player2:Player ,infinityStone: InfinityStone):
        super().__init__()
        self.__is_alive = True

    def update_health(self, player:Player): # call this in update rounds every round for each player and it returns the clue if available
        if self.__is_alive:
            if len(self.__rounds_left) > 0:
                self.__rounds_left -= 1
            guardian = self.get_guardians_present()[0]
            if guardian.belongs_to_player == player:
                reduce_health =  guardian.set_health(guardian.get_health() - self.__damage)
                if reduce_health != None:
                    return reduce_health
                else:
                    clue = Feedback("clue", self.get_clue())
                    return clue
