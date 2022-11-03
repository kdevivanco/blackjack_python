from classes.deck import Deck

bicycle = Deck()

bicycle.show_cards()

for card in bicycle.cards:
    print (card.point_val)
