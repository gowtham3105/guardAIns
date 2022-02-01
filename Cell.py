class Cell:
    def __init__(self, coordinates):
        self.__coordinates = coordinates
        self.__guardian_present = None
        self.__neighbour_cells = []

    def add_neighbour_cell(self, cell: 'Cell'):
        self.__neighbour_cells.append(cell)

    def get_neighbour_cells(self):
        return self.__neighbour_cells

    def get_coordinates(self):
        return self.__coordinates

    def __str__(self) -> str:
        return str(self.__coordinates)
