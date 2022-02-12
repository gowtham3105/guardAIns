from .Clue import Clue

class Beast(Clue):
    def __init__(self, cell):
        super().__init__(cell)
        self.__cell_type = "Beast"

    def update_health(self):
        pass
