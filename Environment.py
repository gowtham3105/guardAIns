import random

from Action import Action
from Cell import Cell
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
        self.__width = None
        self.__height = None
        self.__printable_matrix = None

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
        matrix = []
        wall = ['|'] + ['-', '|'] * n
        printable_matrix = [wall, ]
        self.__height = m
        self.__width = n

        for i in range(m):
            temp_matrix = []
            for j in range(n):
                temp_matrix.append(Cell((i, j)))
            matrix.append(temp_matrix)
            cell_spaces = ['|'] + [' ', '|'] * n
            printable_matrix.append(cell_spaces.copy())
            printable_matrix.append(wall.copy())

        for i in range(m):
            for j in range(n):
                possible_neighbours = []
                if i + 1 < m:
                    if matrix[i + 1][j] not in matrix[i][j].get_neighbour_cells():
                        possible_neighbours.append([1, 0])
                if i - 1 >= 0:
                    if matrix[i - 1][j] not in matrix[i][j].get_neighbour_cells():
                        possible_neighbours.append([-1, 0])
                if j + 1 < n:
                    if matrix[i][j + 1] not in matrix[i][j].get_neighbour_cells():
                        possible_neighbours.append([0, 1])
                # if j-1 >= 0:
                #     if matrix[i][j-1] not in matrix[i][j].get_neighbour_cells():
                #         possible_neighbours.append([0, -1])
                # print(possible_neighbours)

                if not len(possible_neighbours):
                    continue
                random_choice = random.choice(possible_neighbours)

                matrix[i + random_choice[0]][j + random_choice[1]].add_neighbour_cell(matrix[i][j])
                matrix[i][j].add_neighbour_cell(
                    matrix[i + random_choice[0]][j + random_choice[1]])
                printable_matrix[2 * i + 1 + random_choice[0]
                                 ][2 * j + 1 + random_choice[1]] = ' '

        self.__graph = matrix
        self.__printable_matrix = printable_matrix

    def print_graph(self):
        if not self.__printable_matrix:
            return False
        for i in range(len(self.__printable_matrix)):
            print("".join(self.__printable_matrix[i]))

        return True

    def movegen(self, player: Player) -> dict:
        # sent as input for the player object, it contains the neighboring cells,
        # current locations of troops, health of troops and feedback.

        return_dict = {
            # 0 - up, 1 - left, 2 - down, 3 - right
            'gamora': [[], [], [], []],
            'drax': [[], [], [], []],
            'rocket': [[], [], [], []],
            'groot': [[], [], [], []],
            'star_lord': [[], [], [], []]
        }
        for key in player.guardians.keys():
            # for all directions
            current_guardian_obj = player.guardians[key]
            for i in range(4):  # 0 - up, 1 - left, 2 - down, 3 - right
                dir_ver = 0
                dir_hor = 0
                current_coordinates = current_guardian_obj.coordinates.get_coordinates()
                current_cell = current_guardian_obj.coordinates
                if i == 0 or i == 2:
                    dir_ver = i - 1  # dir_ver = -1 or 1
                else:
                    dir_hor = i - 2  # dir_hor = -1 or 1
                for x in range(1, current_guardian_obj.vision+1):
                    possible_neighbour = (
                        current_coordinates[0] + dir_ver*x, current_coordinates[1] + dir_hor*x)
                    if possible_neighbour[0] < 0 or possible_neighbour[0] >= self.__height or possible_neighbour[1] < 0 or possible_neighbour[1] >= self.__width:
                        break
                    if self.__graph[possible_neighbour[0]][possible_neighbour[1]] in current_cell.get_neighbour_cells():
                        return_dict[key][i].append(
                            self.__graph[possible_neighbour[0]][possible_neighbour[1]])
                        current_cell = self.__graph[possible_neighbour[0]
                                                    ][possible_neighbour[1]]
                    else:
                        break
        return return_dict

    def update_rounds(self):
        pass

    def validate_action(self, action: Action) -> bool:
        pass
