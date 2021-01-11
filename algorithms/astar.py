from heapq import heapify, heappop, heappush
from node import Node


def astar(startNode, targetNode, grid):
    # gCost - distance from starting node
    # hCost - distance from target node
    #  fCost = gCost + hCost

    # openSet contains nodes that are candidates for examining
    openSet = []
    # closedSet contains nodes that have already been examined
    closedSet = set()
    startNode.distance = 0

    # openSet.add(startNode)
    heappush(openSet, (startNode.distance, startNode))
    while openSet:
        curr = heappop(openSet)
        closedSet.add(curr)

        if curr == targetNode:
            return

        neighbors = getNeighbors(curr, grid)
        for neighbor in neighbors:
            gCost = curr.gCost + 1  # 1 is the distance between neighbor and curr node
            if neighbor not in openSet or gCost < neighbor.gCost:
                neighbor.gCost = gCost
                neighbor.heuristicCost = manhattanDistance(
                    neighbor, targetNode)
                neighbor.distance = neighbor.gCost + neighbor.heuristicCost
                heappush(openSet, (neighbor.distance, neighbor))
                neighbor.prev = curr


def manhattanDistance(node, targetNode):
    # Use this heuristic when move only in 4 directions (left, right, up, down)
    return abs(node.row - targetNode.row) + abs(node.col - targetNode.col)


def euclideanDistance(startNode, endNode):
    # used when move in any direction
    return sqrt((startNode.row - endNode.row) ** 2 + (startNode.col - endNode.col) ** 2)


def getNeighbors(node, grid):
    neighbors = []

    for new_position in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        node_position = (
            node.row + new_position[0], node.col + new_position[1])

        #  within range and walkable
        if node_position[0] < len(grid) and node_position[0] >= 0 and node_position[1] >= 0 and node_position[1] < len(grid) and grid[node_position[0]][new_position[1]] == 0:
            neighbors.append(Node(new_position[0], new_position[1]))

    return neighbors
