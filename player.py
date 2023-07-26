"""This module defines the Player class, representing a player in a card game."""

from exceptions import GameOverException


class Player:
    """
    The Player class represents a player in a card game.
    """
    def __init__(self):
        """
        Initialize the Player object with an empty list to store cards.
        """
        self.cards = []

    def take_card(self, card):
        """
        Add a card to the player's hand.

        Parameters:
        - card (Card): The card to be added to the player's hand.
        """
        self.cards.append(card)

    def calculate_points(self):
        """
        Calculate the total points of the player's hand.

        Returns:
        int: The total points of the player's hand.

        Raises:
        GameOverException: If the total points exceed 21 (bust).
        """
        points = 0

        numbers_of_aces = len([card for card in self.cards if card.value == 'Ace'])

        if numbers_of_aces == 2 and len(self.cards) == 2:
            return 21

        if numbers_of_aces == 1 and len(self.cards) == 2:
            points = 10

        for card in self.cards:
            if card.value == 'Ace':
                points += 1
            elif card.value in ['Jack', 'Queen', 'King']:
                points += 10
            else:
                points += card.value

        if points > 21:
            raise GameOverException('Numbers of points exceeded!')

        return points
