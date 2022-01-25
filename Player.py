from Guardians.Drax import Drax
from Guardians.Gamora import Gamora
from Guardians.Groot import Groot
from Guardians.Rocket import Rocket
from Guardians.StarLord import StarLord
from .Cell import Cell
from .State import State


class Player:
    player_id = 0
    base_coordinates = None
    gamora = None
    rocket = None
    groot = None
    drax = None
    star_lord = None

    def __init__(self, pid, base_coord: Cell):
        self.player_id = pid
        self.base_coordinates = base_coord
        self.gamora = Gamora(self, base_coord, True)
        self.rocket = Rocket(self, base_coord, True)
        self.groot = Groot(self, base_coord, True)
        self.drax = Drax(self, base_coord, True)
        self.star_lord = StarLord(self, base_coord, True)

    def bot(self, state: State):
        # return the action object
        action = None
        return action
