from __future__ import annotations
from copy import deepcopy

class Board:
    def __init__(self, tiles: list[list[int]]):
        if not tiles or any(len(row) != len(tiles) for row in tiles):
            raise ValueError("Board must be a non-empty square 2D list")

        self.tiles = deepcopy(tiles)
        self.n = len(tiles)
        self.board = [tile for row in tiles for tile in row]
        """
        Initializes the board from a given n-by-n list of lists.
        Each element is an integer in the range 0 to n^2 - 1, where 0 represents the blank space.
        """

    def dimension(self) -> int:
        return self.n

    def hamming(self) -> int:
        return sum(1 for i, val in enumerate(self.board) if val != 0 and val != i + 1)
    """
    Returns the number of tiles that are not in their goal position.
    Do not count the blank (0) in the Hamming score.
    """

    def manhattan(self) -> int:
        distance = 0
        for i, val in enumerate(self.board):
            if val == 0:
                continue
            target_row, target_col = divmod(val - 1, self.n)
            curr_row, curr_col = divmod(i, self.n)
            distance += abs(curr_row - target_row) + abs(curr_col - target_col)
        return distance
    """
    Returns the sum of the Manhattan distances (vertical + horizontal)
    from the tiles to their goal positions.
    """

    def is_goal(self) -> bool:
        return self.board[:-1] == list(range(1, self.n * self.n))
    """
    Returns True if the board is the goal board.
    """

    def neighbors(self) -> list[Board]: # you might have to import annotations from __future__
        def in_bounds(r, c):
            return 0 <= r < self.n and 0 <= c < self.n

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        zero_idx = self.board.index(0)
        zero_row, zero_col = divmod(zero_idx, self.n)

        for dr, dc in dirs:
            new_row, new_col = zero_row + dr, zero_col + dc
            if in_bounds(new_row, new_col):
                new_idx = new_row * self.n + new_col
                new_board = self.board[:]
                new_board[zero_idx], new_board[new_idx] = new_board[new_idx], new_board[zero_idx]
                new_tiles = [new_board[i:i+self.n] for i in range(0, len(new_board), self.n)]
                neighbors.append(Board(new_tiles))

        return neighbors
    """
    Returns an iterable (e.g., generator) of all neighboring boards.
    A neighbor is a board obtained by sliding a tile into the empty space.
    Depending on the position of the blank, there will be 2, 3, or 4 neighbors.
    """

    def twin(self) -> Board:
        twin_board = self.board[:]

        for i in range(len(twin_board)):
            if twin_board[i] != 0:
                for j in range(i + 1, len(twin_board)):
                    if twin_board[j] != 0:
                        twin_board[i], twin_board[j] = twin_board[j], twin_board[i]
                        tiles = [twin_board[k:k+self.n] for k in range(0, len(twin_board), self.n)]
                        return Board(tiles)

        return self  # fallback (should not happen)
    """
    Returns a board that is a twin of the current board — obtained by swapping any pair
    of tiles (the blank should not be swapped).
    This is useful for detecting unsolvable puzzles.
    """

    "helper methods"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Board):
            return False
        return self.board == other.board

    def __str__(self) -> str:
        rows = [" ".join(f"{val:2d}" for val in self.tiles[i]) for i in range(self.n)]
        return f"{self.n}\n" + "\n".join(rows)

if __name__ == '__main__':
    initial = [
        [8, 1, 3],
        [4, 0, 2],
        [7, 6, 5]
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    b = Board(initial)
    print("Initial board:")
    print(b)
    print("Hamming:", b.hamming())
    print("Manhattan:", b.manhattan())
    print("Is goal:", b.is_goal())

    print("\nNeighbors:")
    for neighbor in b.neighbors():
        print(neighbor)

    print("\nTwin:")
    print(b.twin())

    print("Equals self:", b == b)
    print("Equals twin:", b == b.twin())
    print("Equals new Board:", b == Board(initial))
    # Add some basic tests to verify your Board methods.
    # For example, read a board from an input, print it, and check distances.