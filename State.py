class State:
    def __init__(self, state: str, parent: State = None, action: Action = None) -> None:
        self.__state = state
        self.__parent = parent
        self.__action = action
        self.__children = []
