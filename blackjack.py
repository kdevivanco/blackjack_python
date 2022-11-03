class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points") 
        


import random 

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def show_values(self):
        for card in self.cards:
            print(card.point_val)
    
    def sacar_carta(self):
        carta_elegida = random.choice(self.cards)
        self.cards.remove(carta_elegida)  
        return carta_elegida


class Humano:
    def __init__(self,name):
        self.name = name
        self.hand = []
        
    def elegir_carta(self,maso):
        carta_jugador = maso.sacar_carta()
        self.hand.append(carta_jugador) #agrega la nueva carta a la mano
     #imprime que carta salio
    
    def sumar_carta(self,maso):
        self.card_sum = 0
        for card in self.hand:
            self.card_sum += card.point_val
        return self.card_sum #Suma del valor de las cartas FALTA AGREGAR CONDICION PARA As
    
    def show_hand(self):
        for card in self.hand:
            print (card.card_info())

class Dealer(Humano):
    
    def __init__(self,name):
        super().__init__(name)
        
    def mano_menor(self,maso):
        self.card_sum = 0
        for card in self.hand:
            self.card_sum += card.point_val
        
        if self.card_sum < 16:
            self.elegir_carta(maso)
    

class Jugador(Humano):
    def __init__(self,name):
        super().__init__(name)
    
    def preguntar(self,maso):
        respuesta = input('Quieres sacar una carta más? Si/No: ')
        
        if respuesta.lower() == 'si':
            self.elegir_carta(maso)
        
        else:
            pass 


class Game:
    def __init__(self):
        self = self
        
    def check_points(self,dealer,jugador):
        if jugador.card_sum > 21:
            print('BUST, you lost')
        elif dealer.card_sum > 21:
            print('Dealer busted, you win')
            
        elif dealer.card_sum > jugador.card_sum:
            print(f'YOU LOST Dealer: {dealer.card_sum} | Player: {jugador.card_sum}')
        
        elif dealer.card_sum < jugador.card_sum:
            print(f'YOU WIN Dealer: {dealer.card_sum} | Player: {jugador.card_sum}')
            
        elif dealer.card_sum < jugador.card_sum and jugador.card_sum == 21: 
            print(f'YOU WIN BLACKJACK Dealer: {dealer.card_sum} | Player: {jugador.card_sum}') 
            
        





