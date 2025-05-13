import sys
from Board import *
from Solver import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python solver.py [input_file]")
        return
    
    
    with open(sys.argv[1], 'r') as f:
        # The first integer is the board dimension n.
        n = int(f.readline().strip())
        tiles = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            tiles.append(row)

    initial_board = Board(tiles)
    solver = Solver(initial_board)

    if not solver.is_solvable():
        print("No solution possible")
    else:
        print("Minimum number of moves =", solver.moves())
    for board in solver.solution():
        print(board)
    
if __name__ == '__main__':
    main()
