import imp
from Guardians.Gamora import Gamora
from Player import Player
from Guardians.Drax import Drax
from Guardians.Gamora import Gamora
from Guardians.Groot import Groot
from Guardians.Rocket import Rocket
from Guardians.StarLord import StarLord


class State:
    # This class is data given for users.  for now penality score, feedback, movegen, player's troops info.
    def __init__(self, movegen: dict, feedback, penalty_score, round_no, player: Player) -> None:
        self.__feedback = feedback
        self.__penalty_score = penalty_score
        self.__round_no = round_no
        self.__movegen = movegen
        self.__player = player
    def get_movegen(self):
        return self.__movegen

    def get_feedback(self):
        return self.__feedback

    def get_penality_score(self):
        return self.__penalty_score

    def json(self):
        movegen_as_json = {}
        troops_name = ['Gamora', 'Rocket', 'Groot', 'Drax', 'StarLord']
        for troop_name, troop in self.__movegen.items():
            neighbours = []
            for cell_list in troop:
                side = []
                for cell in cell_list:
                    side.append({str(cell): cell.__class__.__name__, 'guardians_present': [{i.belongs_to_player,i.__class__.__name__} for i in cell.get_guardians_present()]})
                neighbours.append(side)
            movegen_as_json[troop_name] ={"coordinates": str(self.__player.get_guardian_by_type(troop_name).coordinates), "health": self.__player.get_guardian_by_type(troop_name).health ,"neighbour_cells": neighbours}
        
        feedback_as_json = []
        for feed in self.__feedback:
            feedback_as_json.append(feed.json())
        
        return {
            "movegen": movegen_as_json,
            "feedback": feedback_as_json,
            "penalty_score": self.__penalty_score,
            "round_no": self.__round_no
        }
