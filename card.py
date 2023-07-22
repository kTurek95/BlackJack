"""Black Jack Python game - class Card"""


class InvalidColor(Exception):
    """Exception when color is invalid"""


class InvalidValue(Exception):
    """Exception when value is invalid"""


class Card:
    """Card abstraction"""
    possible_colors = {
        'spades': '\u2664',
        'diamonds': '\u2662',
        'hearts': '\u2661',
        'clubs': '\u2667'
    }

    possible_values = list(range(2, 11)) + [
        'Ace',
        'Jack',
        'Queen',
        'King'
    ]

    def __init__(self, color, value):
        if color not in self.possible_colors:
            raise InvalidColor

        self.color = self.possible_colors[color]

        if value not in self.possible_values:
            raise InvalidValue('Invalid card value')

        self.value = value

    def __repr__(self):
        return f'{self.value} -> {self.color}'
