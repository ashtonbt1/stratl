from classes.card import Card

card1 = Card('Roberto', 'Clemente', 1960, 'PIT', None)

print(card1.first_name)

try:
    card2 = Card('Roberto', 'Clemente', '1800', 'PIN', 4)
except ValueError as e:
    print(f"{type(e)}: {e}")
except TypeError as e:
    print(f"{type(e)}: {e}")