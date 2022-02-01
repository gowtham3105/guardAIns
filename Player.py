from Cell import Cell
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
    guardians = {'gamora': None,
                 'drax': None,
                 'rocket': None,
                 'groot': None,
                 'star_lord': None
                 }

    def __init__(self, pid, base_coord: Cell):
        self.player_id = pid
        self.base_coordinates = base_coord
        self.gamora = Gamora(self, base_coord, True)
        self.guardians['gamora'] = Gamora
        self.rocket = Rocket(self, base_coord, True)
        self.guardians['rocket'] = Rocket
        self.groot = Groot(self, base_coord, True)
        self.guardians['groot'] = Groot
        self.drax = Drax(self, base_coord, True)
        self.guardians['drax'] = Drax
        self.star_lord = StarLord(self, base_coord, True)
        self.guardians['star_lord'] = StarLord

    def bot(self, state: State):
        # return the action object
        action = None
        return action
