import collections
from random import choice

Card = collections.namedtuple('card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JOAK')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        self._cards_test = [10]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, posititon):
        return self._cards[posititon]
deck = FrenchDeck()

print("Stop")