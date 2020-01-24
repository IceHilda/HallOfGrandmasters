# Description
import numpy as np


class BlackJack:
    # define draw and stand.
    def __init__(self):
        # Numbers 1-13 repeated x4
        cards = np.arange(1, 14)
        self.deck = list(np.repeat(cards, 4))
        self.hand = []
        self.dealer_hand = []

    def draw(self, n=2):
        for x in range(n):
            self.hand.append(self.deck[0])
            popped = self.deck.pop(0)
            self.deck.append(popped)


    def stand(self):
        pass

    def shuffle(self):
        np.random.shuffle(self.deck)


Game = BlackJack()
Game.shuffle()
print(Game.deck)
Game.draw()
print(Game.deck)
print(Game.hand)

