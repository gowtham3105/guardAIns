from Player import Player
from .Clue import Clue


class Beast(Clue):
    def __init__(self):
        super().__init__()
        self.__is_alive = True
        self.__damage = 1
        self.__rounds_left = 3
    
    def update_health(self, player:Player): # call this in update rounds every round for each player and it returns the clue if available
        if self.__is_alive:
            if len(self.__rounds_left) > 0:
                self.__rounds_left -= 1
            for guardian in self.get_guardians_present():
                if guardian.belongs_to_player == player:
                    guardian.set_health(guardian.get_health() - 25)
            if self.__rounds_left == 0:
                self.__is_alive = False
                self.is_clue_active = False
                return { "clue": self.get_clue() }
