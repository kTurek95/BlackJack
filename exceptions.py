"""This module defines custom exception classes related to game over scenarios in a game."""


class GameOverException(Exception):
    """
    Base class for game over exceptions in the game.
    """


class GameOverUserException(Exception):
    """
    Exception class for game over scenarios caused by user actions.
    """


class GameOverCroupierException(Exception):
    """
     Exception class for game over scenarios caused by the croupier (dealer) actions.
    """
