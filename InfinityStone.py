from Cells.Cell import Cell
from Feedback import Feedback


class InfinityStone:
    def __init__(self, coordinates: Cell):
        self.__coordinates = coordinates
        self.__guardian = None
        self.__is_returned_to_base = False

    def update_coordinates(self):
        if not self.__is_returned_to_base:
            if self.__guardian is not None:
                if self.__guardian.is_alive():
                    self.__coordinates = self.guardianObject.get_coordinates()
                    return Feedback("infinity_stone_moved"),
                else:
                    self.__guardian = None
                    return Feedback("infinity_stone_dropped"), Feedback(
                        "guardian_died_and_infinity_stone_dropped", {"guardian": self.__guardian.get_type()}), \
                           self.__guardian.get_belongs_to_player().get_player_id()
            else:
                if self.__coordinates.get_guardians_present() == 1:
                    self.__guardian = self.__coordinates.get_guardians_present()[0]
                    return Feedback("infinity_stone_picked_up"), Feedback("guardian_picked_up_infinity_stone", {
                        "guardian": self.__guardian.get_type()}), \
                           self.__guardian.get_belongs_to_player().get_player_id()

                else:
                    self.__guardian = None
                    return None, None, None

    def get_coordinates(self):
        return self.__coordinates

    def get_guardian(self):
        return self.__guardian

    def set_guardian(self, guardian):
        self.__guardian = guardian

    def is_returned_to_base(self):
        return self.__isReturnedToBase

    def set_returned_to_base(self, is_returned_to_base):
        self.__is_returned_to_base = is_returned_to_base
