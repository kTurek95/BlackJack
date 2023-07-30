"""This module defines the Game class,
which simulates a simple card game between a player and a croupier."""

from deck import Deck
from player import Player
import exceptions as ex


class Game:
    """
    The Game class represents a simple card game between a player and a croupier.
    """
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @ staticmethod
    def _print_menu():
        """
        Print the game menu with available actions for the player.
        """
        print('Co chcesz zrobić?')
        print('0 - odbieram kartę')
        print('1 - pasuje')

    def _croupier_plays(self, points):
        """
        Simulate the croupier's turn in the game.

        Parameters:
        - points (int): The points obtained by the player.

        Returns:
        int: The total points obtained by the croupier.
        """
        croupier = Player()
        while croupier.calculate_points() < points:
            croupier.take_card(self.deck.hit())
            print('KRUPIER: ')
            print(croupier.cards)
            print(croupier.calculate_points())

        return croupier.calculate_points()

    def _user_plays(self):
        """
        Simulate the player's turn in the game.

        Returns:
        int: The total points obtained by the player.
        """
        user = Player()
        for _ in range(2):
            card = self.deck.hit()
            user.take_card(card)

        while True:
            print(user.cards)
            print(user.calculate_points())
            self._print_menu()
            choice = input('Wybierz 0 lub 1: ')
            if choice == '0':
                self.deck.hit()
                user.take_card(self.deck.hit())
            elif choice == '1':
                break
            else:
                print('Dokonano nieprawidłowego wyboru!')

        return user.calculate_points()

    def play(self):
        """
        Start and play the game.

        Raises:
        GameOverUserException: If the game ends due to a user action.
        GameOverCroupierException: If the game ends due to a croupier action.

        Note:
        This method is intended to be the entry point for playing the game.
        """
        try:
            user_points = self._user_plays()
            self._croupier_plays(user_points)
        except ex.GameOverException as error:
            raise ex.GameOverUserException from error
        try:
            self._croupier_plays(user_points)
        except ex.GameOverException as error:
            raise ex.GameOverCroupierException from error

        print('Koniec gry, wygrana krupiera!')
