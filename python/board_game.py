import numpy as np
from constants import EMPTY

class BoardGame:
    ROWS = 0
    COLS = 0

    def reset(self):
        self.board = np.zeros((self.ROWS, self.COLS), dtype=int)
        return self.board

    def is_winner(self, player):
        return False

    def is_draw(self):
        return False

    def get_valid_actions(self):
        actions = [(i, j) for i in range(self.ROWS) for j in range(self.COLS) if self.board[i, j] == EMPTY]
        return actions