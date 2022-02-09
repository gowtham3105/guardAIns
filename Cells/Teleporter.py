from .Cell import Cell


class Teleporter(Cell):
    def __init__(self, cell: Cell):
        super().__init__(cell.get_coordinates())
        self.__cell_type = "Teleporter"

    def generate_destination(self):
        pass

    def update_location(self):
        pass
