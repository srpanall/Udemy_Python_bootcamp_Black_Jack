from hands import *


class Person():
    """docstring for Person"""
     def __init__(self):
        self.hand = Hand()
        

    def check_hand(self):

        if self.hand.value > 21:
            print('Dealer busts. Player wins')
        

class Dealer():

    def __init__(self):
        self.hand = DealerHand()

    def hand_action(self):
        if self.hand.value < 16:
            self.hand = self.hand.deal_card()

    def check_hand(self):
        if self.hand.value < 16:
            self.hand = self.hand.deal_card()
        el


class Player():

    def __init__(self, name, stake):
        self.name = name
        self.stake = stake
        self.hand = Hand()
        self.bet = 0

    def place_bet(self):
        self.bet = int(input('Place your bet.\n'))
        while self.bet > self.stake:
            self.bet = int(input("You can't cover that bet, please place a different bet.\n"))

    def hand_action(self):
        while True:
            action = input('Do you want to hit or stand?/nTyep  H for hit and S for stand').upper()
            if self.hand.value > 21:
                print('You busted')
                return False
            elif action == 'H':
                self.hand.deal_card()
            elif action == 


deck = Deck(suits, values, 5)

for index, card in enumerate(deck.cards):
    temp_card = Card(*card)
    print(temp_card)
    if index == 10:
        break

deck = Deck(suits, values, 5)

for index, card in enumerate(deck.cards):
    temp_card = Card(*card)
    print(temp_card)
    if index == 3:
        break

# hand = Hand()

# dealers_hand = DealerHand()

# for _ in range(2):
#     hand.deal_card(Card(*deck.deal_card()))
#     dealers_hand.deal_card(Card(*deck.deal_card()))


# print(dealers_hand)
# print(dealers_hand.value)

# print(hand)

# print(hand.value)
