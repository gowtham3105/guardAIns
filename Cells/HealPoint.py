from Cells.Cell import Cell


class HealPoint(Cell):
    def __init__(self, cell: Cell):
        super().__init__(cell.get_coordinates(), cell.get_guardians_present(), cell.get_neighbour_cells(),
                         Cell.HealPoint)
        self.__cell_type = "HealPoint"
        self.rounds_present = None
    
    def remove_guardian_from_cell(self, guardian):
        if guardian in self.__guardian_present:
            self.__guardian_present.remove(guardian)
            del self.rounds_present[guardian]
        else:
            raise (ValueError("Guardian not present in the cell"))
            print("Guardian not found in the cell")
    
    def update_rounds_present(self):
        for guardian in(self.__guardian_present):
            if guardian in self.rounds_present:
                self.rounds_present[guardian]+=1
            else:
                self.rounds_present = 1

    def update_health(self):
        for guardian in(self.__guardian_present):
            if self.rounds_present >= 5 and guardian.get_health() < 300:
                guardian.set_health(300)
            elif self.rounds_present[guardian]<5:
                print("Need to stay longer")
            else:
                print("Health is maximum")