
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
        try:
            action_type = json_data["action_type"]
            troop = json_data["troop"]
            target = json_data["target"]
            player_id = json_data["player_id"]
            player_password = json_data["player_password"]
            round_no = json_data['round_no']
            return cls(action_type, troop, target, round_no, player_id, player_password)
        except KeyError:
            print("KeyError: Invalid json data", json_data)
            return False
        except:
            print("Unexpected error", json_data)
            return False

    def __init__(self, action_type, troop, target_coordinates: tuple, round_no, player_id, player_password) -> None:
        if action_type in (Action.MOVE, Action.ATTACK, Action.SPECIAL):
            self.__action_type = action_type

        if troop in Action.TROOPS:
            self.__troop = troop

        self.__target = target_coordinates
        self.__is_valid = False
        self.__round_no = round_no
        self.__player_id = player_id
        self.__player_password = player_password

    def get_action_type(self) -> str:
        return self.__action_type

    def get_guardian_type(self):
        return self.__troop

    def get_target(self, graph) -> tuple:
        return graph[self.__target[0]][self.__target[1]]

    def set_action_type(self, action_type: str) -> None:
        self.__action_type = action_type

    def get_player_id(self):
        return self.__player_id

    def get_round_no(self):
        return self.__round_no

    def json(self) -> dict:
        return {
            "action_type": self.__action_type,
            "troop": self.__troop,
            "target": self.__target,
            "player_id": self.__player_id,
            "player_password": self.__player_password,
            "round_no": self.__round_no
        }
