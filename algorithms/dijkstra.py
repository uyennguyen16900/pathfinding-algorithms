from heapq import heapify, heappop, heappush


def dijkstra(start, target, grid):
    startNode = Node(start[0], start[1])
    targetNode = Node(target[0], target[1])

    visitedNodes = []
    startNode.distance = 0
    unvisitedNodes = getAllNodes(grid)
    while unvisitedNodes:
        closestNode = heappop(unvisitedNodes)[1]
        closestNode.isVisited = True
        if closestNode.distance == float('inf'):
            return
        if closestNode == targetNode:
            return
        visitedNodes.append(closestNode)
        # update the closest node's neighbors
        neighbors = getNeighbors(closestNode, grid)
        for neighbor in neighbors:
            if not neighbor.isVisited:
                neighbor.distance = distance + 1
                neighbor.prev = closestNode


def getNeighbors(node, grid):
    neighbors = []

    for new_position in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        node_position = (
            node.row + new_position[0], node.col + new_position[1])
        #  within range and walkable
        if node_position[0] < len(grid) and node_position[0] >= 0 and node_position[1] >= 0 and node_position[1] < len(grid) and grid[node_position[0]][new_position[1]] == 0:
            neighbors.append(Node(new_position[0], new_position[1]))

    return neighbors


def getAllNodes(grid):
    nodes = []
    for row in range(len(grid)):
        for col in range(len(row)):
            if grid[row][col] == 0:
                heappush(nodes, (grid[row][col].distance, grid[row][col]))
    return nodes
