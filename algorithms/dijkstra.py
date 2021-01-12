from heapq import heapify, heappop, heappush
from node import Node


def dijkstra(start, target, grid):
    startNode = Node(start[0], start[1])
    targetNode = Node(target[0], target[1])

    visitedNodes = []
    startNode.distance = 0
    # unvisitedNodes = getAllNodes(grid)
    unvisitedNodes = []
    heappush(unvisitedNodes, (startNode.distance, startNode))
    while unvisitedNodes:
        closestNode = heappop(unvisitedNodes)[1]
        closestNode.isVisited = True
        if closestNode == targetNode:
            return getPath(startNode, closestNode, grid)
        visitedNodes.append(closestNode)
        # update the closest node's neighbors
        neighbors = getNeighbors(closestNode, grid)
        for neighbor in neighbors:
            if not neighbor.isVisited:
                neighbor.distance = closestNode.distance + 1
                neighbor.prev = closestNode
                heappush(unvisitedNodes, (neighbor.distance, neighbor))


def getNeighbors(node, grid):
    neighbors = []

    for new_position in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        node_position = (
            node.row + new_position[0], node.col + new_position[1])
        #  within range and walkable
        if node_position[0] < len(grid) and node_position[0] >= 0 and node_position[1] >= 0 and node_position[1] < len(grid[0]) and grid[node_position[0]][node_position[1]] == 0:
            neighbors.append(Node(node_position[0], node_position[1]))

    return neighbors


def getAllNodes(grid):
    nodes = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                node = Node(row, col)
                heappush(nodes, (node.distance, node))
    return nodes


def getPath(startNode, targetNode, grid):
    path = []
    curr = targetNode
    print(curr)
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
print(dijkstra(start, end, maze))
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
