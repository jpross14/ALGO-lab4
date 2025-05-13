from Board import *
from __future__ import annotations 

class Solver: # you might have to import annotations from __future__
    def __init__(self, initial: Board):
        """
        Find the solution to the initial board using the A* algorithm.
        If the initial board is None, raise a ValueError.
        """
        pass

    def is_solvable(self) -> bool:
        """
        Returns True if the initial board is solvable.
        A well-known fact: the puzzle is solvable if and only if the goal board is
        reachable from the initial board. One efficient approach is to run two simultaneous
        A* searches: one on the initial board and one on its twin (obtained by swapping any
        pair of non-blank tiles). Exactly one of these searches will yield a solution.
        """
        pass

    def moves(self) -> int:
        """
        Returns the minimum number of moves required to solve the puzzle,
        or -1 if the puzzle is unsolvable.
        """
        pass

    def solution(self) -> list[Board]:
        """
        Returns a list of Board objects representing the sequence of moves from the
        initial board to the goal board, if the puzzle is solvable. Otherwise, return None.
        """
        pass

    


