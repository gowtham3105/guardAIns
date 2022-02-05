class Feedback:
    # list of strings based on the events that happened in this round, and a method to display it
    feedbacks = {
        "invalid_action": {
            "code": "INVALID_ACTION",
            "message": "Invalid action, Your Score is decreased by this."
        },
        "timeout": {
            "code": "TIMEOUT",
            "message": "Time is up, Your Score is decreased by this."
        },
        "error": {
            "code": "ERROR",
            "message": "Something went wrong, Your Score is decreased by this."
        },
        "you_have_been_attacked": {
            "code": "YOU_HAVE_BEEN_ATTACKED",
            "message": "You have been attacked, Your Troops health is decreased by this."
        },

    }

    def __init__(self, feedback_code, data=None) -> None:
        self.__feedback_code = self.feedbacks[feedback_code]["code"]
        self.__feedback_message = self.feedbacks[feedback_code]["message"]
        self.__data = str(data) if data is not None else None

    def get_feedback_code(self) -> str:
        return self.__feedback_code

    def get_feedback_message(self) -> str:
        return self.__feedback_message

    def get_data(self) -> str:
        return self.__data
