from random import shuffle

suits = [u'\u2664', u'\u2661', u'\u2662', u'\u2667']

values = {'A': 11, 'J': 10, 'K': 10, 'Q': 10}

for item in range(2, 11):
    values[str(item)] = item


class Deck():
    '''Creates 1 or more shuffled decks of cards'''

    def __init__(self, suits, values, decks=1):
        self.cards = [(suit, val) for suit in suits for val in values] * decks
        shuffle(self.cards)

    def __str__(self):
        return ' '.join([str(item) for item in self.cards])

    def deal_card(self):
        card_dealt = self.cards[0]
        self.cards.remove(self.cards[0])
        return card_dealt[0], card_dealt[1]


class Card():
    '''Creates a card object given a value and a suite and adds a method
    for printing a card.'''

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.card_layout = [' _____ ',
                            f'|{self.value.ljust(2)}   |',
                            f'|  {self.suit}  |',
                            '|_____|']

    def __str__(self):
        return '\n'.join(self.card_layout)


if __name__ == "__main__":
    deck = Deck(suits, values, 5)

    for index, card in enumerate(deck.cards):
        temp_card = Card(*card)
        print(temp_card)
        if index == 3:
            break
