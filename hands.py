from cards import *


class Hand():

    def __init__(self):
        self.cards = list()
        self.values = list()
        self.value = 0

    def evaluate_hand(self):
        val_0 = sum([values[item] for item in self.values])
        if val_0 == 21 and len(self.values) == 2:
            return (21, 'Black Jack')
        hand_value = [val_0, ]
        for val in self.values:
            if val == 'A':
                hand_value.append(hand_value[-1] - 10)
        if 21 in hand_value:
            return 21
        else:
            return min(hand_value)

    def deal_card(self, card):
        self.cards.append(card)
        self.values.append(card.value)
        self.value = self.evaluate_hand()

    def __str__(self):
        hand_layout = ['   '.join([card.card_layout[n] for card in self.cards]) for n in range(4)]
        hand_out = '\n'.join(hand_layout)
        return hand_out


class DealerHand(Hand):
    """docstring for DealerHand"""

    def __str__(self):
        first_card = Card(u'\u0488', ' ')
        temp_hand = [first_card, ] + self.cards[1:]
        hand_layout = ['   '.join([card.card_layout[n] for card in temp_hand]) for n in range(4)]
        hand_out = '\n'.join(hand_layout)
        return hand_out


deck = Deck(suits, values, 5)


hand = Hand()

dealers_hand = DealerHand()

for _ in range(2):
    hand.deal_card(Card(*deck.deal_card()))
    dealers_hand.deal_card(Card(*deck.deal_card()))


print(dealers_hand)
print(dealers_hand.value)

print(hand)

print(hand.value)
