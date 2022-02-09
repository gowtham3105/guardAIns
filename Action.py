class Action:
    # UPDATE ACTION TO SEND the acting players, drax, gamora.. objects directly with get_guardian(),
    # and update get_coordinate to send cell object directly
    MOVE = "MOVE"
    ATTACK = "ATTACK"
    SPECIAL = "SPECIAL"
    TROOPS = ('Groot', 'Rocket', 'Gamora', 'StarLord', 'Drax')

    def __init__(self, action_type, troop, target_coordinates: tuple, player_id, player_secret) -> None:
        if action_type in (Action.MOVE, Action.ATTACK, Action.SPECIAL):
            self.__action_type = action_type

        if troop in Action.TROOPS:
            self.__troop = troop

        self.__target = target_coordinates
        self.__is_valid = False
        self.player_id = player_id
        self.player_secret = player_secret

    def get_action_type(self) -> str:
        return self.__action_type

    def get_troop(self) -> TROOPS:
        return self.__troop

    def get_guardian_type(self):
        return self.__troop

    def get_target(self, graph) -> tuple:
        return graph[self.__target[0]][self.__target[1]]

    def set_action_type(self, action_type: str) -> None:
        self.__action_type = action_type
