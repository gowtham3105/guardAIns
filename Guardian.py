from Cell import Cell
# from Player import Player


class Guardian:
    health = 0
    attack_damage = 0
    vision = 0
    speed = 0
    cooldown = 0
    belongs_to_player = None
    is_alive = 0
    coordinates = None

    def __init__(self, belongs, init_coordinates: Cell, alive=True):
        self.belongs_to_player = belongs
        self.coordinates = init_coordinates
        self.is_alive = alive

    def attack(self, cell: Cell):
        # check if cell has an enemy i.e guardian from opposite team
        # update health
        return 0

    def update_cooldown(self):
        # called from environment, cold own is updated after every round
        return 0

    def mark_as_dead(self, alive=False):
        # marks a player as dead
        self.is_alive = False
    def set_coordinates(self, coordinates: Cell):
        self.coordinates = coordinates