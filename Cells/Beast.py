from .Clue import Clue


class Beast(Clue):
    def __init__(self):
        super().__init__()
        self.__cell_type = "Beast"

    def update_health(self):
        pass
