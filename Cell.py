from Guardian import Guardian

class Cell:
    def __init__(self, coordinates):
        self.__coordinates = coordinates
        self.__guardian_present =  [] # This should have the guardian sub class object of the guardian present in the cell
        self.__neighbour_cells = []
        self.__is_guardian_present = False
        
    def add_neighbour_cell(self, cell: 'Cell'):
        if cell not in self.__neighbour_cells:
            self.__neighbour_cells.append(cell)

    def delete_neighbour_cell(self, cell: 'Cell'):
        if cell in self.__neighbour_cells:
            self.__neighbour_cells.remove(cell)
            
    def get_neighbour_cells(self):
        return self.__neighbour_cells

    def get_coordinates(self):
        return self.__coordinates

    def get_is_guardian_present(self):
        return self.__is_guardian_present

    def update_is_guardian_present(self):
        if(len(self.__guardian_present) > 0):
            self.__is_guardian_present = True
        else:
            self.__is_guardian_present = False

    def set_guardian_present(self, guardian): #this guardian should be of the type Drax, Gamora etc
        self.update_is_guardian_present()
        self.__guardian_present.append(guardian)

    def get_guardians_present(self):  #Returns a list of guardians present in the cell
        return self.__guardian_present

    def __str__(self) -> str:
        return str(self.__coordinates)

    def __repr__(self):
        return "Cell" + str(self.__coordinates)
