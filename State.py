from Cells.Cell import Cell


class State:
    def __init__(self, movegen: dict, feedback, penalty_score, round_no) -> None:
        self.__feedback = feedback
        self.__penalty_score = penalty_score
        self.__round_no = round_no
        # Copy movegen  to avoid reference

        temp_movgen = {}

        for troop_name, troop in movegen.items():
            neighbours = []
            for cell_list in troop:
                side = []
                for cell in cell_list:
                    new_cell = Cell(cell.get_coordinates(), cell.get_guardians_present(), cell.get_neighbour_cells(),
                                    cell.get_cell_type())
                    side.append(new_cell)
                neighbours.append(side)
            temp_movgen[troop_name] = neighbours
        self.__movegen = temp_movgen

        for troop in self.__movegen.values():
            for cell_list in troop:
                for cell in cell_list:
                    cell.remove_neighbours()

        self.__movegen = movegen

    def get_movegen(self):
        return self.__movegen

    def get_feedback(self):
        return self.__feedback

    def get_penality_score(self):
        return self.__penalty_score

    def json(self):
        movegen_as_json = {}
        for troop_name, troop in self.__movegen.items():
            neighbours = []
            for cell_list in troop:
                side = []
                for cell in cell_list:
                    side.append(str(cell))
                neighbours.append(side)
            movegen_as_json[troop_name] = neighbours

        feedback_as_json = []

        for feed in self.__feedback:
            feedback_as_json.append(feed.json())

        return {
            "movegen": movegen_as_json,
            "feedback": feedback_as_json,
            "penalty_score": self.__penalty_score,
            "round_no": self.__round_no
        }
