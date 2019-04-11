from random import shuffle
from class_Card_War import Card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
            shuffle(self.cards)


    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


"""
52枚のカードを順番に表示
deck = Deck()
for card in deck.cards:
    print(card)

"""
