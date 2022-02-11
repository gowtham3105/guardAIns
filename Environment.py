import random
import time

from Action import Action
from Cells.Cell import Cell
from Cells.Teleporter import Teleporter
# from Cells.Cell import Cell
from Feedback import Feedback
from Player import Player
from State import State


class Environment:
    def __init__(self, room_id, start_time, height, width, max_penality_score, player_timeout, max_rounds) -> None:
        self.__env = {'__name__': 'GuardAIns', '__version__': '0.1'}
        self.__room_id = room_id
        self.__start_time = start_time
        self.__graph = None
        self.__rounds = 0
        self.__currentState = None
        self.__player1_feedback = None
        self.__player2_feedback = None
        self.__currentActions = []
        self.__player1 = None
        self.__player2 = None
        self.__width = width
        self.__height = height
        self.__printable_matrix = None
        self.__player1_actions = []
        self.__player2_actions = []
        self.__player1_penality_score = max_penality_score
        self.__player2_penality_score = max_penality_score
        self.__player_timeout = player_timeout
        self.__winner = None
        self.__game_over = False
        self.__max_rounds = max_rounds

    def get_env(self):
        return self.__env

    def get_start_time(self):
        return self.__start_time

    def get_room_id(self):
        return self.__room_id

    def get_graph(self):
        return self.__graph

    def get_rounds(self):
        return self.__rounds

    def get_current_state(self) -> State:
        return self.__currentState

    def get_feedback(self) -> Feedback:
        return self.__feedback

    def get_player1(self) -> Player:
        return self.__player1

    def get_player2(self) -> Player:
        return self.__player2

    def set_player1(self, player1: Player) -> None:
        self.__player1 = player1

    def set_player2(self, player2: Player) -> None:
        self.__player2 = player2

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_player1_actions(self):
        return self.__player1_actions

    def get_player2_actions(self):
        return self.__player2_actions

    def get_player1_penality_score(self):
        return self.__player1_penality_score

    def get_player2_penality_score(self):
        return self.__player2_penality_score

    def get_winner(self):
        return self.__winner

    def add_action_to_player1(self, action: Action) -> None:
        self.__player1_actions.append(action)

    def add_action_to_player2(self, action: Action) -> None:
        self.__player2_actions.append(action)

    def create_graph(self) -> None:

        matrix = []
        wall = ['|'] + ['-', '|'] * self.__width
        printable_matrix = [wall, ]

        for i in range(self.__height):
            temp_matrix = []
            for j in range(self.__width):
                temp_matrix.append(Cell((i, j)))
            matrix.append(temp_matrix)
            cell_spaces = ['|'] + [' ', '|'] * self.__width
            printable_matrix.append(cell_spaces.copy())
            printable_matrix.append(wall.copy())

        stack = [matrix[0][0]]
        visited = [[0 for _ in range(self.__width)] for _ in range(self.__height)]
        while len(stack):
            current_cell = stack.pop()
            if visited[current_cell.get_coordinates()[0]][current_cell.get_coordinates()[1]] > 1:
                continue
            visited[current_cell.get_coordinates()[0]][current_cell.get_coordinates()[1]] += 1
            possible_neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            random.shuffle(possible_neighbours)
            # possible_neighbours = random.choices(possible_neighbours, k=3)

            for neighbour in possible_neighbours:
                if neighbour[0] + current_cell.get_coordinates()[0] < 0 \
                        or neighbour[0] + current_cell.get_coordinates()[0] >= self.__height:
                    continue
                if neighbour[1] + current_cell.get_coordinates()[1] < 0 \
                        or neighbour[1] + current_cell.get_coordinates()[1] >= self.__width:
                    continue

                if visited[neighbour[0] + current_cell.get_coordinates()[0]][
                    neighbour[1] + current_cell.get_coordinates()[1]] > 1:
                    continue
                if matrix[neighbour[0] + current_cell.get_coordinates()[0]][
                    neighbour[1] + current_cell.get_coordinates()[1]] in stack:
                    continue

                current_cell.add_neighbour_cell(matrix[neighbour[0] + current_cell.get_coordinates()[0]][
                                                    neighbour[1] + current_cell.get_coordinates()[1]])
                matrix[neighbour[0] + current_cell.get_coordinates()[0]][
                    neighbour[1] + current_cell.get_coordinates()[1]].add_neighbour_cell(current_cell)
                stack.append(matrix[neighbour[0] + current_cell.get_coordinates()[0]][
                                 neighbour[1] + current_cell.get_coordinates()[1]])
                printable_matrix[
                    2 * (current_cell.get_coordinates()[1]) + 1 + neighbour[1]][
                    2 * (current_cell.get_coordinates()[0]) + 1 + neighbour[0]] = ' '

        self.__graph = matrix
        self.__printable_matrix = printable_matrix

    def print_graph(self):
        if not self.__printable_matrix:
            return False
        for i in range(len(self.__printable_matrix)):
            print("".join(self.__printable_matrix[i]))

        return True

    def is_graph_connected(self):
        all_cells = []

        for i in range(self.__height):
            for j in range(self.__width):
                all_cells.append(self.__graph[i][j])

        queue = [self.__graph[0][0]]
        visited = []

        while len(queue):
            node = queue.pop(0)

            for cell in node.get_neighbour_cells():

                if cell in visited:
                    continue

                if cell in all_cells:
                    all_cells.remove(cell)

                visited.append(cell)
                queue.append(cell)

        if len(all_cells) == 0:
            return True
        else:
            return False

    def place_special_cells(self, no_of_teleporters, no_of_healpoints, no_of_clues, no_of_beasts):
        for i in range(no_of_teleporters):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            self.__graph[0][0] = Teleporter(self.__graph[0][0])
            pass

    def movegen(self, player: Player) -> dict:
        # sent as input for the player object, it contains the neighboring cells,
        # current locations of troops, health of troops and feedback.

        return_dict = {
            # 0 - up, 1 - left, 2 - down, 3 - right
            'Gamora': [[], [], [], []],
            'Drax': [[], [], [], []],
            'Rocket': [[], [], [], []],
            'Groot': [[], [], [], []],
            'StarLord': [[], [], [], []]
        }
        for key in player.get_guardians().keys():
            # for all directions
            current_guardian_obj = player.get_guardians()[key]
            for i in range(4):  # 0 - up, 1 - left, 2 - down, 3 - right
                dir_ver = 0
                dir_hor = 0
                current_coordinates = current_guardian_obj.coordinates.get_coordinates()
                current_cell = current_guardian_obj.coordinates
                if i == 0 or i == 2:
                    dir_ver = i - 1  # dir_ver = -1 or 1

                else:
                    dir_hor = i - 2  # dir_hor = -1 or 1
                for x in range(1, current_guardian_obj.vision + 1):
                    possible_neighbour = (
                        current_coordinates[0] + dir_ver * x, current_coordinates[1] + dir_hor * x)
                    if possible_neighbour[0] < 0 or possible_neighbour[0] >= self.__height or possible_neighbour[
                        1] < 0 or possible_neighbour[1] >= self.__width:
                        break
                    if self.__graph[possible_neighbour[0]][possible_neighbour[1]] in current_cell.get_neighbour_cells():
                        return_dict[key][i].append(
                            self.__graph[possible_neighbour[0]][possible_neighbour[1]])
                        current_cell = self.__graph[possible_neighbour[0]
                        ][possible_neighbour[1]]
                    else:
                        break
        return return_dict

    def update_rounds(self, sio):
        while self.get_start_time() - time.time() > 0:
            print("Time left: ", self.get_start_time() - time.time())
            time.sleep(1)

        print('Starting Update Rounds')
        print(self.get_player1(), self.get_player2())

        if self.get_player1() is None:
            if self.get_player2() is None:
                # both players are dead
                print("Both players are Not Connected")
                self.__winner = None
                self.__game_over = True
                return True
            else:
                # player 2 is alive
                self.__winner = self.get_player2()
                self.__game_over = True
                print("Player 2 is the Winner")
                return True
        else:
            if self.get_player2() is None:
                # player 1 is alive
                self.__winner = self.get_player1()
                self.__game_over = True
                print("Player 1 is the Winner")
                return True

        while True:
            if self.__player1_penality_score < 0 <= self.__player2_penality_score:  # player 2 wins
                self.__winner = self.__player2
                self.__game_over = True
                print("Player 2 is the Winner")
                return True
            if self.__player2_penality_score < 0 <= self.__player1_penality_score:  # player 1 wins
                self.__winner = self.__player1
                self.__game_over = True
                print("Player 1 is the Winner")
                return True
            if self.__player1_penality_score < 0 and self.__player2_penality_score < 0:  # draw
                self.__winner = None
                self.__game_over = True
                print("Draw")
                return True

            if self.__max_rounds < self.__rounds:  # If Max Rounds is reached
                if self.get_player1_penality_score() > self.get_player2_penality_score():
                    self.__winner = self.__player1
                    print("Player 1 is the Winner")
                elif self.get_player1_penality_score() < self.get_player2_penality_score():
                    self.__winner = self.__player2
                    print("Player 2 is the Winner")
                else:
                    self.__winner = None
                    print("Draw")
                self.__game_over = True

                print("Game Over")
                return True
            player1_state = State(self.movegen(self.get_player1()), self.__player1_feedback,
                                  self.__player1_penality_score, self.get_rounds())
            player2_state = State(self.movegen(self.get_player2()), self.__player2_feedback,
                                  self.__player2_penality_score, self.get_rounds())

            player1_error = False
            player2_error = False

            player1_action = None
            player2_action = None

            try:
                sio.call("action", to=self.get_player1().get_socket_id(), data=player1_state.json(),
                         timeout=self.__player_timeout)
                if len(self.__player1_actions):
                    player1_action = self.__player1_actions[-1]
                    if player1_action.get_round_no() != self.get_rounds():
                        raise RuntimeError("Player 1 Action Data Inconsistent")
                else:
                    raise RuntimeError('Player 1 Action Not found')
                print("Player 1 Action: ", player1_action, type(player1_action))
            except TimeoutError:
                self.__player1_feedback = Feedback("timeout")
                player1_error = True
                self.reduce_score(self.get_player1().get_player_id(), "timeout")
            except Exception as e:
                print(e)
                self.__player1_feedback = Feedback("error", e)
                player1_error = True
                self.reduce_score(self.get_player1().get_player_id(), "error")

            try:
                sio.call("action", to=self.get_player2().get_socket_id(), data=player2_state.json(),
                         timeout=self.__player_timeout)
                if len(self.__player2_actions):
                    player2_action = self.__player2_actions[-1]
                    if player2_action.get_round_no() != self.get_rounds():
                        raise RuntimeError("Player 2 Action Data Inconsistent")
                else:
                    raise RuntimeError('Player 2 Action Not found')
                print("Player 2 Action: ", player2_action, type(player2_action))
            except TimeoutError:
                self.__player2_feedback = Feedback("timeout")
                player2_error = True
                self.reduce_score(self.get_player2().get_player_id(), "timeout")
            except Exception as e:
                print(e)
                self.__player2_feedback = Feedback("error", e)
                player2_error = True
                self.reduce_score(self.get_player2().get_player_id(), "error")

            # print(player1_action, player2_action)
            self.execute_action(player1_action, player2_action, player1_error, player2_error)
            self.__rounds += 1

        return True

    def validate_action(self, action: Action) -> bool:
        # Always check if the acting guardian is alive or not
        if action is None:
            print("Action is None")
            return False

        player = action.get_player_id()
        if player == self.get_player1().get_player_id():
            guardian = self.__player1.get_guardian_by_type(action.get_guardian_type())
        elif player == self.get_player2().get_player_id():
            guardian = self.__player2.get_guardian_by_type(action.get_guardian_type())
        else:
            guardian = None

        if guardian is not None:
            if guardian.is_alive():
                if action.get_action_type() == "ATTACK":
                    if ((guardian.coordinates.get_coordinates()[0] - guardian.vision) <=
                        action.get_target_coordinates()[0] <=
                        (guardian.coordinates.get_coordinates()[0] + guardian.vison)) and (
                            guardian.coordinates.get_coordinates()[1] - guardian.vision <=
                            action.get_target_coordinates()[1] <=
                            guardian.coordinates.get_coordinates()[1] + guardian.vision):
                        return True
                    print("Target out of range")
                    return False
                elif action.get_action_type() == "MOVE":
                    if ((guardian.coordinates.get_coordinates()[0] - guardian.speed) <= action.get_target_coordinates()[
                        0] <=
                        (guardian.coordinates.get_coordinates()[0] + guardian.speed)) and (
                            guardian.coordinates.get_coordinates()[1] - guardian.speed <=
                            action.get_target_coordinates()[1] <=
                            guardian.coordinates.get_coordinates()[1] + guardian.speed):
                        return True
                    print("Target out of range MOVE")
                    return False
                elif action.get_action_type() == "SPECIAL":
                    # check all parameters for special actions once it is updated
                    return True
            else:
                print("Guardian is dead")
                return False
        else:
            print("Guardian not found")
            return False

    def execute_action(self, player1_action: Action, player2_action: Action, player1_error: bool, player2_error: bool):
        print("player1: ", self.get_player1().get_guardians(), "player2", self.__player2.get_guardians())
        player1_error = False
        player2_error = False
        if not self.validate_action(player1_action):
            player1_error = True
            self.reduce_score(self.get_player1().get_player_id(), 'invalid_action')
            print("player1", self.get_player1_penality_score())
        if not self.validate_action(player2_action):
            player2_error = True
            self.reduce_score(self.get_player2().get_player_id(), 'invalid_action')
            print("player2", self.get_player2_penality_score())

        print(player1_error, player2_error, "errors execute action")
        if not player1_error:
            if player1_action.get_action_type() == "MOVE":
                guardian = self.__player1.get_guardian_by_type(
                    player1_action.get_guardian_type())  # update it to return
                # guardian object directly
                print("player1: ", self.get_player1().get_guardians(), "player2", self.__player2.get_guardians())
                print("Here")
                guardian.get_coordinates().remove_guardian_from_cell(guardian)
                print("player1: ", self.get_player1().get_guardians(), "player2", self.__player2.get_guardians())
                print("Here11")
                guardian.set_coordinates(player1_action.get_target(self.__graph))
                print("player1: ", self.get_player1().get_guardians(), "player2", self.__player2.get_guardians())

                guardian.get_coordinates().add_guardian_to_cell(guardian)

            elif player1_action.get_action_type == "Attack":
                guardians_present = player1_action.get_target().get_guardians_present()
                our_guadian = player1_action.get_guardian()
                for guardian in guardians_present:
                    # if multiple enemy __guardians are present then attack all, if none of them are there then for __guardians present would be empty
                    if (guardian.belongs_to == self.__player2):
                        # update get_troop to return guardian object after checking if the guardian is not dead
                        guardian.set_health(guardian.get_health() - our_guadian.get_damage())
                        if (guardian.get_health() <= 0):
                            guardian.is_alive = False
                            guardian.set_health(0)

                    # Set appropriate feedback for other player


            elif (player1_action.get_action_type == "Special"):
                player1_action.get_guardian().special_ability()  # since we are getting the guradian object corresponding to the sub class, we can directly call the special ability

        return "f"

    def reduce_score(self, player: str, feedback_code: str):

        FEEDBACKS_CODES = {
            "timeout": -1,
            "error": -2,
            "invalid_action": -2,
        }

        if feedback_code in FEEDBACKS_CODES.keys():
            if player == self.get_player1().get_player_id():
                self.__player1_penality_score += FEEDBACKS_CODES[feedback_code]
            elif player == self.get_player2().get_player_id():
                self.__player2_penality_score += FEEDBACKS_CODES[feedback_code]
            else:
                raise Exception("Invalid player id")
        else:
            raise ValueError("Invalid feedback code")
