"""Test module for deck.py"""

from deck import Deck
from card import Card


def test_creation():
    """
    Test the creation of a new deck.

    This test verifies that a new deck is created correctly, containing
    52 unique cards.
    """
    my_deck = Deck()
    assert len(my_deck.cards) == 52


def test_deck():
    """
    Test the composition of a deck.

    This test checks whether the deck contains cards of each color
    (hearts, diamonds, clubs, spades) in the correct amounts (13 cards of each color).
    """
    my_deck = Deck()
    cards = [(card.value, card.color) for card in my_deck.cards]

    for color in Card.possible_colors.values():  # zapisujemy.values,
        # ponieważ potrzebujemy wartości, którymi są znaczki
        cards_in_color =[card for card in cards if card[1] == color]
        assert len(cards_in_color) == 13


def test_shuffle():
    """
   Test the shuffling of the deck.

   This test verifies that shuffling the deck results in a new order of the cards.
   It checks if the shuffled deck is different from the original one.
   """
    my_deck = Deck()
    cards = my_deck.cards[:]  # w ten sposób robi się kopie listy
    my_deck.shuffle()  # tasujemy karty w talii
    assert cards != my_deck.cards


def test_deck_hit():
    """
    Test the 'hit' method of the deck.

    This test checks if the 'hit' method correctly removes and returns the last card from the deck.
    """
    my_deck = Deck()
    last_card = my_deck.cards[-1]
    card = my_deck.hit()
    assert last_card == card


def test_deck_count_cards():
    """
    Test the count of cards in the deck after hitting.

    This test verifies that the number of cards in the deck decreases by one
    after calling the 'hit' method. It also checks
    that the drawn card is no longer present in the deck.
    """
    my_deck = Deck()
    card = my_deck.hit()
    assert len(my_deck.cards) == 51
    assert card not in my_deck.cards
