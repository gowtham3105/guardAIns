# from Action import Action


class State:
    def __init__(self, state: str, parent, action) -> None:
        self.__state = state
        self.__parent = parent
        self.__action = action
        self.__children = []
