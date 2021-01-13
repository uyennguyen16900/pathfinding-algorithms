from heapq import heapify, heappop, heappush
from node import Node


def dijkstra(start, target, grid):
    startNode = Node(start[0], start[1])
    targetNode = Node(target[0], target[1])
    startNode.distance = 0

    visitedNodes = []
    # unvisitedNodes = getAllNodes(grid)
    unvisitedNodes = []
    heappush(unvisitedNodes, (startNode.distance, startNode))
    while len(unvisitedNodes) > 0:
        closestNode = heappop(unvisitedNodes)[1]
        visitedNodes.append(closestNode)

        if closestNode == targetNode:
            print(closestNode.prev)
            return getPath(startNode, closestNode, grid)
        # update the closest node's neighbors
        neighbors = getNeighbors(closestNode, grid)
        for neighbor in neighbors:
            distance = closestNode.distance + 1

            if neighbor in visitedNodes or distance < neighbor.distance:
                neighbor.distance = distance
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
    return curr.row, curr.col
    while curr != startNode:
        path.append((curr.row, curr.col))
        grid[curr.row][curr.col] = '.'
        curr = curr.prev

    return path[::-1]


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
start = (0, 0)
end = (0, 9)

# print(dijkstra(start, end, maze))
