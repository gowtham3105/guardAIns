from Cells.Cell import Cell


class HealPoint(Cell):
    def __init__(self, cell: Cell):
        super().__init__(cell.get_coordinates(), cell.get_guardians_present(), cell.get_neighbour_cells(),
                         Cell.HealPoint)
        self.__cell_type = "HealPoint"
        self.rounds_present = None

    def update_rounds_present(self):
        pass

    def update_health(self):
        pass
