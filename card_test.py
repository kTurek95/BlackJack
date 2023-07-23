"""Test module for card.py"""

import pytest
from card import Card, InvalidValue, InvalidColor # zaimportowanie klasy Card z modułu card


def test_creation():
    """
    Test the creation of a card with valid color and value.
    It checks if the card's color and value are set correctly.
    """
    card = Card('hearts', 'Ace')
    assert card.color == '♡'
    assert card.value == 'Ace'


def test_creation_wrong_value():
    """
    Test the creation of a card with an invalid value.
    It checks if the proper 'InvalidValue' exception is raised.
    """
    with pytest.raises(InvalidValue) as message:  # dzięki temu zapisowi pytest wie
        # , że ma się wyświetlić błąd, oczekujemy, że pojawi się taki właśnie wyjątek
        assert message == 'Invalid card value!'


def test_creation_wron_color():
    """
    Test the creation of a card with an invalid color.
    It checks if the proper 'InvalidColor' exception is raised.
    """
    with pytest.raises(InvalidColor) as message:
        assert message == 'Invalid card value!'


def test_card_representation():
    """
    Test the representation of a card in its string format.
    It checks if the card's string representation matches the expected format.
    """
    assert repr(Card('spades', 'Ace')) == 'Ace -> ♤'
    assert repr(Card('diamonds', 'Ace')) == 'Ace -> ♢'
    assert repr(Card('hearts', 'Ace')) == 'Ace -> ♡'
    assert repr(Card('clubs', 'Ace')) == 'Ace -> ♧'
