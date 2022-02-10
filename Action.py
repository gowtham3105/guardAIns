
class Action:
    # UPDATE ACTION TO SEND the acting players, drax, gamora.. objects directly with get_guardian(),
    # and update get_coordinate to send cell object directly
    MOVE = "MOVE"
    ATTACK = "ATTACK"
    SPECIAL = "SPECIAL"
    INTERACT = "INTERACT"
    TROOPS = ('Groot', 'Rocket', 'Gamora', 'StarLord', 'Drax')

    @classmethod
    def get_obj_from_json(cls, json_data: dict):
        action_type = json_data["action_type"]
        troop = json_data["troop"]
        target = json_data["target"]
        player_id = json_data["player_id"]
        player_password = json_data["player_password"]
        return cls(action_type, troop, target, player_id, player_password)

    def __init__(self, action_type, troop, target_coordinates: tuple, player_id, player_password) -> None:
        if action_type in (Action.MOVE, Action.ATTACK, Action.SPECIAL):
            self.__action_type = action_type

        if troop in Action.TROOPS:
            self.__troop = troop

        self.__target = target_coordinates
        self.__is_valid = False
        self.player_id = player_id
        self.player_password = player_password

    def get_action_type(self) -> str:
        return self.__action_type

    def get_guardian_type(self):
        return self.__troop

    def get_target(self, graph) -> tuple:
        return graph[self.__target[0]][self.__target[1]]

    def set_action_type(self, action_type: str) -> None:
        self.__action_type = action_type

    def json(self) -> dict:
        return {
            "action_type": self.__action_type,
            "troop": self.__troop,
            "target": self.__target,
            "player_id": self.player_id,
            "player_password": self.player_password
        }
