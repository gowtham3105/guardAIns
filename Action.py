import re
from Guardians.Drax import Drax
from Guardians.Gamora import Gamora
from Guardians.Groot import Groot
from Guardians.Rocket import Rocket
from Guardians.StarLord import StarLord
from Player import Player
from Cell import Cell

class Action:
    #UPDATE ACTION TO SEND the acting players, drax, gamora.. objects directly with get_guardian(), 
    #and update get_coordinate to send cell object directly
    MOVE = "MOVE"
    ATTACK = "ATTACK"
    SPECIAL = "SPECIAL"
    TROOPS = (Groot, Rocket, Gamora, StarLord, Drax)

    def __init__(self, action_type, troop: TROOPS, target_coordianates:Cell, acting_player:Player) -> None:
        if action_type in (Action.MOVE, Action.ATTACK, Action.SPECIAL):
            self.__action_type = action_type

        if isinstance(troop, Action.TROOPS):
            self.__troop = troop

        self.__target = target_coordianates
        self.__is_valid = False
        self.acting_player = acting_player

    def get_action_type(self) -> str:
        return self.__action_type

    def get_troop(self) -> TROOPS:
        return self.__troop

    def get_guardian(self):
        if(self.__troop == TROOPS[0]):
            return self.acting_player.groot
        elif(self.__troop == TROOPS[1]):
            return self.acting_player.rocket
        elif(self.__troop == TROOPS[2]):
            return self.acting_player.gamora
        elif(self.__troop == TROOPS[3]):
            return self.acting_player.star_lord
        elif(self.__troop == TROOPS[4]):
            return self.acting_player.drax



    def get_target(self) -> tuple:
        return self.__target

    def set_action_type(self, action_type: str) -> None:
        self.__action_type = action_type
