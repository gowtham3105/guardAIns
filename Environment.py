from Action import Action
from Feedback import Feedback
from Player import Player
from State import State


class Environment:
    def __init__(self) -> None:
        self.__env = {'__name__': 'GuardAIns', '__version__': '0.1'}
        self.__graph = None
        self.__rounds = 0
        self.__currentState = None
        self.__feedback = None
        self.__currentActions = []
        self.___player1 = None
        self.___player2 = None

    def get_env(self):
        return self.__env

    def get_graph(self):
        return self.__graph

    def get_rounds(self):
        return self.__rounds

    def get_current_state(self) -> State:
        return self.__currentState

    def get_feedback(self) -> Feedback:
        return self.__feedback

    def get_player1(self) -> Player:
        return self.___player1

    def get_player2(self) -> Player:
        return self.___player2

    def set_player1(self, player1: Player) -> None:
        self.___player1 = player1

    def set_player2(self, player2: Player) -> None:
        self.___player2 = player2

    def createGraph(self, m: int, n: int) -> None:
        pass

    def movgen(self, player: Player) -> list[State]:
        pass

    def update_rounds(self):
        pass

    def validate_action(self, action: Action) -> bool:
        pass
