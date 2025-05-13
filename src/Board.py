from __future__ import annotations

class Board:
    def __init__(self, tiles: list[list[int]]):
        """
        Initializes the board from a given n-by-n list of lists.
        Each element is an integer in the range 0 to n^2 - 1, where 0 represents the blank space.
        """
        pass

    def dimension(self) -> int:
        """
        Returns the board dimension n.
        """
        pass

    def hamming(self) -> int:
        """
        Returns the number of tiles that are not in their goal position.
        Do not count the blank (0) in the Hamming score.
        """
        pass

    def manhattan(self) -> int:
        """
        Returns the sum of the Manhattan distances (vertical + horizontal)
        from the tiles to their goal positions.
        """
        pass

    def is_goal(self) -> bool:
        """
        Returns True if the board is the goal board.
        """
        pass

    def neighbors(self) -> list[Board]: # you might have to import annotations from __future__
        """
        Returns an iterable (e.g., generator) of all neighboring boards.
        A neighbor is a board obtained by sliding a tile into the empty space.
        Depending on the position of the blank, there will be 2, 3, or 4 neighbors.
        """
        pass

    def twin(self) -> Board:
        """
        Returns a board that is a twin of the current board — obtained by swapping any pair
        of tiles (the blank should not be swapped).
        This is useful for detecting unsolvable puzzles.
        """
        pass

    if __name__ == '__main__':
        pass
        # Add some basic tests to verify your Board methods.
        # For example, read a board from an input, print it, and check distances.