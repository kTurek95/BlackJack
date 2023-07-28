"""Test module for player.py"""

from player import Player
from card import Card


def test_calculate_player_points():
    """
   Test the calculate_points method of the Player class with two number cards.

   The player has two number cards: 2 of spades and 5 of hearts.
   The total points should be 7.

   This test verifies that the calculate_points method calculates the correct total points.
   """
    card = Card('spades', 2)
    card2 = Card('hearts', 5)

    player = Player()
    player.take_card(card)
    player.take_card(card2)

    assert player.calculate_points() == 7


def test_calculate_player_points_two_aces():
    """
    Test the calculate_points method of the Player class with two Ace cards.

    The player has two Ace cards, which can be counted as 11 points each without busting.
    The total points should be 21.

    This test verifies that the calculate_points method handles two Ace cards correctly.
    """
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 'Ace')

    player = Player()
    player.take_card(card)
    player.take_card(card2)

    assert player.calculate_points() == 21


def test_calculate_player_points_one_ace_two_cards():
    """
    Test the calculate_points method of the Player class with one Ace and one number card.

    The player has one Ace and one number card (2 of hearts).
    The total points should be 13 (Ace as 11, 2 as 2).

    This test verifies that the calculate_points method handles the combination of cards correctly.
    """
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 2)

    player = Player()
    player.take_card(card)
    player.take_card(card2)

    assert player.calculate_points() == 13


def test_calculate_player_points_three_aces():
    """
    Test the calculate_points method of the Player class with three Ace cards.

    The player has three Ace cards, which can be counted as 1 point each without busting.
    The total points should be 3.

    This test verifies that the calculate_points method handles three Ace cards correctly.
    """
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 'Ace')
    card3 = Card('diamonds', 'Ace')

    player = Player()
    player.take_card(card)
    player.take_card(card2)
    player.take_card(card3)

    assert player.calculate_points() == 3
