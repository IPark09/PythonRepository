# Simplified checkers, loosely based on American Checkers:
# - no kings: a checker reaching the far row cannot move any more;
# - no multi-jumps and no mandatory captures;
# - checkers move diagonally forward only: one step or one capture per move;
# - the game ends when a player stops it or the current player has no moves left;
# - result: more captures (points) wins; on equal points the lower total time wins.

from classes import Game

if __name__ == '__main__':
    game = Game()
    game.gaming()