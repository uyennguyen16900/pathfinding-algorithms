class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.distance = float('inf')
        self.isVisited = False
        self.isWall = False
        self.prev = None
        self.gCost = float('inf')
        self.heuristicCost = float('inf')
