from __future__ import annotations 
from Board import *
import heapq
import sys

class SearchNode:
    def __init__(self, board: Board, moves: int, predecessor: SearchNode = None):
        self.board = board
        self.moves = moves
        self.predecessor = predecessor
        self.priority = moves + board.manhattan()

    def __lt__(self, other: SearchNode):
        return self.priority < other.priority


class Solver: # you might have to import annotations from __future__
    def __init__(self, initial: Board):
        if initial is None:
            raise ValueError("Initial board cannot be None")

        self.solvable = False
        self._min_moves = -1
        self._solution_path = []

        self._solve(initial)
    """
    Find the solution to the initial board using the A* algorithm.
    If the initial board is None, raise a ValueError.
    """

    def _solve(self, initial: Board):
        main_pq = []
        twin_pq = []
        heapq.heappush(main_pq, SearchNode(initial, 0))
        heapq.heappush(twin_pq, SearchNode(initial.twin(), 0))

        while True:
            if self._step(main_pq, is_twin=False):
                self.solvable = True
                break
            if self._step(twin_pq, is_twin=True):
                self.solvable = False
                break
    
    def _step(self, pq: list[SearchNode], is_twin: bool) -> bool:
        current = heapq.heappop(pq)

        if current.board.is_goal():
            if not is_twin:
                self._min_moves = current.moves
                self._solution_path = []
                while current:
                    self._solution_path.append(current.board)
                    current = current.predecessor
                self._solution_path.reverse()
            return True

        for neighbor in current.board.neighbors():
            if current.predecessor and neighbor == current.predecessor.board:
                continue
            heapq.heappush(pq, SearchNode(neighbor, current.moves + 1, current))
        return False

    def is_solvable(self) -> bool:
        return self.solvable
    """
    Returns True if the initial board is solvable.
    A well-known fact: the puzzle is solvable if and only if the goal board is
    reachable from the initial board. One efficient approach is to run two simultaneous
    A* searches: one on the initial board and one on its twin (obtained by swapping any
    pair of non-blank tiles). Exactly one of these searches will yield a solution.
    """

    def moves(self) -> int:
        return self._min_moves
    """
    Returns the minimum number of moves required to solve the puzzle,
    or -1 if the puzzle is unsolvable.
    """

    def solution(self) -> list[Board]:
        if not self.solvable:
            return None
        return self._solution_path
    """
    Returns a list of Board objects representing the sequence of moves from the
    initial board to the goal board, if the puzzle is solvable. Otherwise, return None.
    """

def main():
    if len(sys.argv) != 2:
        print("Usage: python solver.py [input_file]")
        return

    with open(sys.argv[1], 'r') as f:
        # parse input...
        n = int(f.readline().strip())
        tiles = [list(map(int, f.readline().split())) for _ in range(n)]

    initial_board = Board(tiles)
    solver = Solver(initial_board)

    if not solver.is_solvable():
        print("No solution possible")
    else:
        print("Minimum number of moves =", solver.moves())
        for board in solver.solution():
            print(board)

if __name__ == "__main__":
    main()