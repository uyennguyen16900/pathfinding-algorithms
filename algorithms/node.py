class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.val = None
        self.distance = float('inf')
        self.isVisited = False
        self.isWall = False
        self.prev = None
        self.gCost = float('inf')
        self.heuristicCost = float('inf')

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __lt__(self, other):
        return self.distance < other.distance
