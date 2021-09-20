from datetime import datetime
from .validation import D20, OneOf, Number, String
from .reference_lists import CARD_TEAMS

# Class references
from .player import Player

class Card:
    # Define validations using the Validator classes
    first_name = String(minsize=1, maxsize=100)
    last_name = String(minsize=1, maxsize=100)
    year = Number(minvalue=1800, maxvalue=datetime.today().year)
    team = OneOf(*CARD_TEAMS)
    steal = D20()

    def __init__(self, first_name, last_name, year, team, steal, player):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.team = team
        self.steal = steal
        self.player = player
