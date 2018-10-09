from random import choice

suits = ['H', 'C', 'D', 'S']
values = {'A': 11, 'J': 10, 'K': 10, 'Q': 10}

for item in range(2, 10):
    values[str(item)] = item



class Dealer():

    def __init__(self):
        self.hand = Hand()


class Player():

    def __init__(self, name, stake):
        self.name = name
        self.stake = stake
        self.hand = Hand()
        self.bet = 0

    def place_bet(self):
        self.bet = int(input('Place your bet.\n'))


class Deck():

    def __init__(self, suits, values):
        self.cards = [(suit, value) for suit in suits for value in values]

    def __str__(self):
        return ' '.join([str(item) for item in self.cards])

    def deal_card(self):
        card_dealt = choice(self.cards)
        self.cards.remove(card_dealt)
        return card_dealt[0], card_dealt[1]


class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.card_layout = [' ___ ',
                            f'|{self.value}  |',
                            f'| {self.suit} |',
                            '|___|']

    def __str__(self):
        return '\n'.join(self.card_layout)


class Hand():

    def __init__(self):
        self.cards = list()
        self.values = list()
        self.value = 0

    def evaluate_hand(self):
        hand_value = sum([values[item] for item in self.values])
        if 'A' in self.values:
            return min(hand_value, hand_value - 10)
        else:
            return hand_value

    def update_hand(self, card):
        self.cards.append(card)
        self.values.append(card.value)
        self.value = self.evaluate_hand()

    def __str__(self):
        hand_out = '\n'.join(['   '.join([card.card_layout[n] for card in self.cards]) for n in range(4)])
        return hand_out


deck = Deck(suits, values)

hand = Hand()

for _ in range(5):
    hand.update_hand(Card(*deck.deal_card()))

print(hand)

print(hand.value)
