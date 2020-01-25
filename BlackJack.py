# Description
import numpy as np


class BlackJack:
    # define draw and stand.
    def __init__(self):
        # Numbers 1-13 repeated x4
        cards = np.arange(2, 15)
        self.deck = list(np.repeat(cards, 4))
        self.hand = []
        self.dealer_hand = []

    def draw(self, the_hand, n=2):
        for x in range(n):
            the_hand.append(self.deck[0])
            popped = self.deck.pop(0)
            self.deck.append(popped)

    def hit_stand(self):
        # need this to loop until stand is returned. While loop has me all fucked up.
        hitting = True
        while hitting:
            print(self.hand, f"(You got: {self.score(self.hand)})")
            print(f"Dealer shows: {self.dealer_hand[0]}")
            choice = input("hit or stand? ")
            if choice == "hit":
                self.draw(self.hand, 1)
                if self.score(self.hand) > 21:
                    print("Busted")
                    break
            if choice == "stand":
                #why is this fine here but in the end of the code it says "total" is undefined?
                hitting = False
                total = sum(self.hand)
                print(total)
                return total

    def shuffle(self):
        np.random.shuffle(self.deck)

    def score(self, the_hand):
        face_cards = [12, 13, 14]
        for x in range(len(the_hand)):
            if the_hand[x] in face_cards:
                the_hand[x] = 10
        subtotal = sum(the_hand)
        # Do something about aces (11)
        if subtotal > 21:
            for x in range(len(the_hand)):
                if the_hand[x] == 11:
                    the_hand[x] = 1
        total = sum(the_hand)
        return total

    def dealer_action(self):
        # Look at the dealer's score

        while self.score(self.dealer_hand) < 17:
            # Hit
            self.draw(self.dealer_hand, 1)

        # Over 21, bust
        if self.score(self.dealer_hand) > 21:
            print("DEALER BUSTED")

    def winner(self):
        me = self.score(self.hand)
        them = self.score(self.dealer_hand)
        if me > them and me <= 21:
            return True
        elif me <= 21 and them > 21:
            return True
        else:
            return False

    def play(self):
        #shuffle
        self.shuffle()
        #deal player 2 cards
        self.draw(self.hand, 2)
        #deal dealer 2 cards
        self.draw(self.dealer_hand, 2)
        # player acts until "stands"
        # (player sees 1 card)
        # if player goes over auto lose
        self.hit_stand()
        #dealer either draws till 17 or stays til 17 or greater.
        self.dealer_action()
        #closest to 21 wins without going over. (aces and face cards)
        if self.winner():
            print("Winner winner chicken dinner")
        else:
            print(f"Dealer sunk your battleship with {self.score(self.dealer_hand)}")

Game = BlackJack()
Game.play()
