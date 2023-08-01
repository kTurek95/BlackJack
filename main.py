"""This module runs a simple card game between a player and a croupier using the Game class."""

from game import Game
import exceptions as ex

try:
    game = Game()
    game.play()
except ex.GameOverCroupierException:
    print('Wygrywa gracz!')
except ex.GameOverUserException:
    print('Wygrywa krupier!')
