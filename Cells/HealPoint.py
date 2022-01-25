from ..Cell import Cell


class HealPoint(Cell):
    def __init__(self):
        super().__init__()
        self.rounds_present = None

    def update_rounds_present(self):
        pass

    def update_health(self):
        pass
