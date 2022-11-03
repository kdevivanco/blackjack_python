from blackjack import *

#1. CREAR MASO DE CARTAS

my_deck = Deck()

#2. CREAR DEALER Y JUGADOR

dealer = Dealer('dealer')

player = Jugador('player')

#3. DEALER DRAWS CARD Y JUGADOR DRAWS CARD 

dealer.elegir_carta(my_deck)
player.elegir_carta(my_deck)

#4. Dealer y jugador show cards

dealer.show_hand()
player.show_hand()

#5. DEALER DRAWS CARD (NO SE MUESTRA) Y JUGADOR DRAWS CARD

dealer.elegir_carta(my_deck)
player.elegir_carta(my_deck)

#6 IMPRIME LA MANO DEL JUGADOR

player.show_hand()

#7 PREGUNTA POR SI QUIERE SACAR UNA MAS...

player.preguntar(my_deck)
player.show_hand()

#8 CHEQUEA QUE LA MANO DEL DEALER SEA MENOR O MAYOR A 16 Y DRAWS (O NO ) CARD

dealer.mano_menor(my_deck)


dealer.sumar_carta(my_deck)
player.sumar_carta(my_deck)

dealer.card_sum
player.card_sum


#9 COMPARA PUNTAJES

game = Game()
game.check_points(dealer,player)