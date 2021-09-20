from .validation import String

class Player:
    # Define validations using the Validator classes
    id = String(minsize=5, maxsize=30)
    first_name = String(minsize=1, maxsize=100)
    last_name = String(minsize=1, maxsize=100)

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
