from heapq import heapify, heappop, heappush


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


def dijkstra(startNode, targetNode, grid):
    visitedNodes = []
    startNode.distance = 0
    unvisitedNodes = getAllNodes(grid)
    while unvisitedNodes:
        closestNode = heappop(unvisitedNodes)[1]
        if self.isWall:
            continue
        if closestNode.distance == float('inf'):
            return visitedNodes
        self.isVisited = True
        if closestNode == targetNode:
            return visitedNodes
        visitedNodes.append(closestNode)

        # update the closest node's neighbors
        row = closestNode.row
        col = closestNode.col
        distance = closestNode.distance
        if col < len(grid[0]) - 1:
            grid[row][col+1].distance = distance + 1
            grid[row][col+1].prev = closestNode
        if col > 0:
            grid[row][col-1].distance = distance + 1
            grid[row][col-1].prev = closestNode
        if row > 0:
            grid[row-1][col].distance = distnace + 1
            grid[row-1][col].prev = closestNode
        if row < len(grid) - 1:
            grid[row+1][col].distance = distance + 1
            grid[row+1][col].prev = closestNode


def getAllNodes(grid):
    nodes = []
    for row in range(len(grid)):
        for col in range(len(row)):
            heappush(nodes, (grid[row][col].distance, grid[row][col]))
    return nodes
