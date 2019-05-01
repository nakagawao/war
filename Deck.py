from random import shuffle
from Card import Card

class Deck:
    def __init__(self):
        self.cards=[]

        for v in range(2,15):
            for s in range(4):
                self.cards.append(Card(v,s))
        shuffle(self.cards)
    def draw_card(self):
        """
        Deckオブジェクト.cardsから要素を返す
        """
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()
