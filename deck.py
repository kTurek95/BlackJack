"""Black Jack Python game - class Deck"""

from random import shuffle  # metoda służąca do losowania
from card import Card


class Deck:
    """Deck abstraction"""
    def __init__(self):
        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.cards.append(
                    Card(color=color, value=value)
                )

    def shuffle(self):
        """
        Shuffles the cards in the deck randomly.
        """
        shuffle(self.cards)

    def hit(self):
        """
         Draws and returns a card from the deck.
        :return: The card drawn from the deck.
        """
        return self.cards.pop()
