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

    def __init__(self, pid, sid, base_coord: Cell):
        self.__player_id = pid,
        self.__socket_id = sid
        self.__connected = True
        self.__base_coordinates = base_coord
        self.__guardians['Gamora'] = Gamora(self, base_coord, True)
        self.__guardians['Rocket'] = Rocket(self, base_coord, True)
        self.__guardians['Groot'] = Groot(self, base_coord, True)
        self.__guardians['Drax'] = Drax(self, base_coord, True)
        self.__guardians['StarLord'] = StarLord(self, base_coord, True)

    def get_guardian_by_type(self, guardian_type: str):
        if guardian_type in self.__guardians:
            return self.__guardians[guardian_type]

    def get_guardians(self):
        return self.__guardians

    def bot(self, state: State):
        # return the action object
        action = Action("MOVE", 'Gamora', (0, 1), 'player1', 'secret')
        return action

    def get_player_id(self):
        return self.__player_id

    def get_socket_id(self):
        return self.__socket_id

    def set_player_id(self, player_id):
        self.__player_id = player_id

    def set_socket_id(self, socket_id):
        self.__socket_id = socket_id

    def is_connected(self):
        return self.__connected

    def set_connected(self, connected):
        self.__connected = connected
