""" 
Code for https://adventofcode.com/2021/day/4
"""

import os

import numpy as np
import numpy.ma as ma


class Board:
    """
    Class to manage Data for AOC Day 4.  Emulates a 5x5 Bingo Board with integers that are called.
    """

    def __init__(self, board: np.ndarray) -> None:
        self.board = board.copy()

        self.called = np.zeros_like(self.board)
        self.size: int = self.board.shape[0]  # Square

    def __repr__(self) -> str:
        return str(self.board)

    def _mark_board(self, lookup_num: int) -> None:
        """Marks a value on the Board as 'called'."""
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row, col] == lookup_num:
                    self.called[row, col] = 1

    def _has_won(self) -> bool:
        """Checks to see if the card has a bingo or not."""
        row_win = (self.called.sum(axis=0) == 5).any()
        col_win = (self.called.sum(axis=1) == 5).any()
        return row_win or col_win

    def _calculate_score(self, call: int) -> int:
        """Calculates the score given the current board has won on `call`."""
        summed_called_vals = ma.masked_array(self.board, mask=self.called).sum()
        return int(call * summed_called_vals)

    def _reset(self) -> None:
        """Resets called numbers for the beginning of the game."""
        self.called = np.zeros_like(self.board)

    @classmethod
    def parse_input(cls, data: list[str]) -> "Board":
        board = np.array([[int(i) for i in row.split(" ") if i] for row in data])
        return cls(board=board)


class Boards:
    """Collection of bingo boards for a game."""

    def __init__(self, boards: list[Board]):
        self.boards = boards

    def __repr__(self) -> str:
        return "\n\n".join([str(board) for board in self.boards])

    def __len__(self) -> int:
        return len(self.boards)

    def _mark_cards(self, call: int) -> None:
        """Marks all cards which have `call`."""
        for board in self.boards:
            board._mark_board(call)

    def _board_has_won(self) -> list[Board]:
        """Returns list of Board if boards have won, else returns None."""
        return [board for board in self.boards if board._has_won()]

    def _remove_board(self, board: Board) -> None:
        """Removes Board from the Boards collection."""
        self.boards.remove(board)

    @classmethod
    def parse_input(cls, data: str) -> "Boards":
        boards_raw = [board.split("\n") for board in data.split("\n\n")]
        boards = [Board.parse_input(board) for board in boards_raw]
        return cls(boards=boards)


if __name__ == "__main__":

    # Initialize Data.
    with open(os.path.abspath("aoc/data/a04_boards.csv"), "r") as f:
        data = f.read()

    with open("aoc/data/a04_calls.csv", "r") as calls_f:
        calls = np.genfromtxt(calls_f, delimiter=",", encoding="utf-8")

    boards = Boards.parse_input(data)
    num_boards = len(boards)

    def nth_to_win(boards: Boards, calls: np.ndarray, n: int = 1) -> tuple[Board, int]:
        """
            Finds the nth board to win at Bingo (or the first if a few have won) and the call it won at.
            Returns (Trivial Board, -1) if no board wins.

        Parameters
        ----------
        boards : Boards
            Boards object, collection of all bingo Board objects.
        calls : np.ndarray
            Array of integer calls for Board objects.

        Returns
        -------
        tuple[Board, int]
            The winning board and the call it won on.  The trivial (zeros) board and -1 if no board wins.
        """

        num_winning_boards = 0
        for call in calls:
            boards._mark_cards(call)
            if len(winning_boards := boards._board_has_won()) > 0:
                num_winning_boards += len(winning_boards)
                for winning_board in winning_boards:
                    boards._remove_board(winning_board)

                if num_winning_boards >= n:
                    return (winning_boards[0], call)

        # Return trivial board if no board wins.
        return (Board(np.zeros(shape=(5, 5))), -1)

    winning_board, winning_call = nth_to_win(boards, calls, n=1)
    solution_a = winning_board._calculate_score(winning_call)

    losing_board, losing_call = nth_to_win(boards, calls, n=(num_boards - 1))
    solution_b = losing_board._calculate_score(losing_call)

    print(f"AOC4a: {solution_a}\nAOC4b: {solution_b}")
