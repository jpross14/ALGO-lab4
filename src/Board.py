from __future__ import annotations

class Board:
    def __init__(self, tiles: list[list[int]]):
        self.tiles = tiles
        self.n = len(tiles)

    def dimension(self) -> int:
        return self.n

    def hamming(self) -> int:
        grid_len = self.n 
        score = 0

        for row in range(grid_len):

            for col in range(grid_len):
                expected_value = row * grid_len + col + 1       
                if self.tiles[row][col] == 0:
                    continue
                if self.tiles[row][col] != expected_value:
                    score += 1

        return score
        

    def manhattan(self) -> int:
        grid_len = self.n 
        score = 0

        for row in range(grid_len):

            for col in range(grid_len):
                if self.tiles[row][col] == 0:
                    continue

                expected_row = (self.tiles[row][col] - 1) // grid_len
                expected_col = (self.tiles[row][col] - 1) % grid_len
                score += abs(expected_row - row) + abs(expected_col - col)

        return score

    def is_goal(self) -> bool:
        if (self.hamming() == 0) and (self.manhattan() == 0):
            return True
        return False

    def neighbors(self) -> list[Board]: # you might have to import annotations from __future__
        neighbors = []
        n = self.n

        for row in range(n):
            for col in range(n):
                if self.tiles[row][col] == 0:
                    blank_row = row
                    blank_col = col
                    break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc 

            if (0 <= new_row < blank_row) and (0 <= new_col < blank_col):
                new_tiles = [row[:] for row in self.tiles]

                new_tiles[row][col]= new_tiles[new_row][new_col]
                new_tiles[new_row][new_col] = new_tiles[row][col]

                neighbor_board = Board(new_tiles, [new_row, new_col])

                neighbors.append(neighbor_board)

        return neighbors

    def twin(self) -> Board:
        """
        Returns a board that is a twin of the current board — obtained by swapping any pair
        of tiles (the blank should not be swapped).
        This is useful for detecting unsolvable puzzles.
        """
        new_tiles = [row[:] for row in self.tiles]
        n = self.n
        
        # Find the first two non-zero tiles to swap
        # We'll look in the first two positions of the first row,
        # unless one of them is zero, then we'll look in the next row
        for i in range(n):
            for j in range(n - 1):
                if new_tiles[i][j] != 0 and new_tiles[i][j + 1] != 0:
                    # Swap these two adjacent tiles
                    new_tiles[i][j], new_tiles[i][j + 1] = new_tiles[i][j + 1], new_tiles[i][j]
                    return Board(new_tiles)
        
        # If we didn't find two adjacent non-zero tiles in the same row (unlikely for n > 1)
        # then look for any two non-zero tiles to swap
        first = None
        for i in range(n):
            for j in range(n):
                if new_tiles[i][j] != 0:
                    if first is None:
                        first = (i, j)
                    else:
                        # Swap with the first found tile
                        new_tiles[first[0]][first[1]], new_tiles[i][j] = new_tiles[i][j], new_tiles[first[0]][first[1]]
                        return Board(new_tiles)
        
        # If we get here, the board is too small or has too many zeros
        return Board(new_tiles)


if __name__ == '__main__':
    # Test 1: 2x2 board
    tiles1 = [[1, 0], [2, 3]]
    board1 = Board(tiles1)
    twin1 = board1.twin()
    B1HammingScore = board1.hamming()
    B1ManhattanScore = board1.manhattan()
    print("Original 2x2 board:")
    print(board1.tiles)
    print("Twin board (should have two non-zero tiles swapped):")
    print(twin1.tiles)
    print(f"Original Hamming Score: {B1HammingScore}")
    print(f"Original Manhattan Score: {B1ManhattanScore}")
    print()
    print("-------------------------------------------------------------------")
    print()

    # Test 2: 3x3 solved board
    tiles2 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    board2 = Board(tiles2)
    twin2 = board2.twin()
    print("Original solved 3x3 board:")
    print(board2.tiles)
    print("Twin board (should have two adjacent non-zero tiles swapped):")
    print(twin2.tiles)
    print(f"Is original board solved? {board2.is_goal()}")
    print(f"Is twin board solved? {twin2.is_goal()}")  # Should be False
    print()
    print("-------------------------------------------------------------------")
    print()

    # Test 3: 3x3 random board
    tiles3 = [[8, 1, 3], [4, 0, 2], [7, 6, 5]]
    board3 = Board(tiles3)
    twin3 = board3.twin()
    print("Original random 3x3 board:")
    print(board3.tiles)
    print("Twin board (should have two non-zero tiles swapped, not the blank):")
    print(twin3.tiles)
    print(f"Original Hamming: {board3.hamming()}")
    print(f"Twin Hamming: {twin3.hamming()}")
    print(f"Original Manhattan: {board3.manhattan()}")
    print(f"Twin Manhattan: {twin3.manhattan()}")
    print()
    print("-------------------------------------------------------------------")
    print()

    # Test 4: Verify twin is different from original
    tiles4 = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
    board4 = Board(tiles4)
    twin4 = board4.twin()
    print("Original board:")
    print(board4.tiles)
    print("Twin board:")
    print(twin4.tiles)
    print("Are they equal?", board4.tiles == twin4.tiles)  # Should be False
    print("Are they twins?", board4.tiles != twin4.tiles)  # Should be True