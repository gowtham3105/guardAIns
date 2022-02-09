from Action import Action
class State:
    def __init__(movegen: dict, feedback, penality_score, self) -> None:
        self.__feedback = feedback
        self.__penality_score = penality_score
        for cell in movegen.values():
            for cell_neighbour in cell.get_neighbours():
                if cell_neighbour not in movegen.values():
                    cell.delete_neighbour(cell_neighbour)
        self.__movegen = movegen
    def get_movegen(self):
        return self.__movegen
    def get_feedback(self):
        return self.__feedback
    def get_penality_score(self):
        return self.__penality_score

