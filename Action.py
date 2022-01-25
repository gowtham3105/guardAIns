from Guardians.Drax import Drax
from Guardians.Gamora import Gamora
from Guardians.Groot import Groot
from Guardians.Rocket import Rocket
from Guardians.StarLord import StarLord


class Action:
    MOVE = "MOVE"
    ATTACK = "ATTACK"
    SPECIAL = "SPECIAL"
    TROOPS = (Groot, Rocket, Gamora, StarLord, Drax)

    def __init__(self, action_type, troop: TROOPS, target_coordianates) -> None:
        if action_type in (Action.MOVE, Action.ATTACK, Action.SPECIAL):
            self.__action_type = action_type

        if isinstance(troop, Action.TROOPS):
            self.__troop = troop

        self.__target = target_coordianates
        self.__is_valid = False

    def get_action_type(self) -> str:
        return self.__action_type

    def get_troop(self) -> TROOPS:
        return self.__troop

    def get_target(self) -> tuple:
        return self.__target

    def set_action_type(self, action_type: str) -> None:
        self.__action_type = action_type
