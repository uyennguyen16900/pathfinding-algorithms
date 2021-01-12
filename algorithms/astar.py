from heapq import heapify, heappop, heappush
from node import Node


def astar(start, target, grid):
    # gCost - distance from starting node
    # hCost - distance from target node
    #  fCost = gCost + hCost
    startNode = Node(start[0], start[1])
    targetNode = Node(target[0], target[1])
    # startNode.gCost, startNode.heuristicCost = 0, 0
    # targetNode.gCost, targetNode.heuristicCost = 0, 0

    # openSet contains nodes that are candidates for examining
    openSet = []
    # closedSet contains nodes that have already been examined
    closedSet = []

    # openSet.add(startNode)
    heappush(openSet, (startNode.distance, startNode))
    while len(openSet) > 0:
        curr = heappop(openSet)[1]
        closedSet.append(curr)
        if curr == targetNode:
            return getPath(startNode, curr, grid)

        neighbors = getNeighbors(curr, grid)
        for neighbor in neighbors:
            gCost = curr.gCost + 1  # 1 is the distance between neighbor and curr node

            if (neighbor.distance, neighbor) not in openSet or gCost < neighbor.gCost:
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
        if node_position[0] < len(grid) and node_position[0] >= 0 and node_position[1] >= 0 and node_position[1] < len(grid[0]) and grid[node_position[0]][node_position[1]] == 0:
            neighbors.append(Node(node_position[0], node_position[1]))

    return neighbors


def getPath(startNode, targetNode, grid):
    path = []
    curr = targetNode
    while curr != startNode:
        path.append((curr.row, curr.col))
        grid[curr.row][curr.col] = '.'
        curr = curr.prev

    return path[::-1]


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (2, 0)
end = (0, 3)

startNode = Node(start[0], start[1])
print(astar(start, end, maze))
print(maze)
# for row in maze:
#     for item in row:
#         if item == 0:
#             print " "
#         elif item == 1:
#             print "X"


# a = []
# heappush(a, (1, 'ji'))
# print((1, 'ji') in a)
