from Action import Action
from Cells.Cell import Cell
from Guardians.Drax import Drax
from Guardians.Gamora import Gamora
from Guardians.Groot import Groot
from Guardians.Rocket import Rocket
from Guardians.StarLord import StarLord
from State import State


class Player:
    player_id = 0
    base_coordinates = None
    gamora = None
    rocket = None
    groot = None
    drax = None
    star_lord = None
    __guardians = {'Gamora': None,
                   'Drax': None,
                   'Rocket': None,
                   'Groot': None,
                   'StarLord': None
                   }

    def __init__(self, pid, base_coord: Cell):
        self.player_id = pid
        self.base_coordinates = base_coord
        self.gamora = Gamora(self, base_coord, True)
        self.__guardians['Gamora'] = self.gamora
        self.rocket = Rocket(self, base_coord, True)
        self.__guardians['Rocket'] = self.rocket
        self.groot = Groot(self, base_coord, True)
        self.__guardians['Groot'] = self.groot
        self.drax = Drax(self, base_coord, True)
        self.__guardians['Drax'] = self.drax
        self.star_lord = StarLord(self, base_coord, True)
        self.__guardians['StarLord'] = self.star_lord

    def get_guardian_by_type(self, guardian_type: str):
        if guardian_type in self.__guardians:
            return self.__guardians[guardian_type]

    def get_guardians(self):
        return self.__guardians

    def bot(self, state: State):
        # return the action object
        action = Action("MOVE", 'Gamora', (0, 1), 'player1', 'secret')
        return action
