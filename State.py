from Action import Action


class State:
    def __init__(self, state: str, parent, action: Action = None) -> None:
        self.__state = state
        self.__parent = parent
        self.__action = action
        self.__children = []
