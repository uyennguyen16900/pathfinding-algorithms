def astar(startNode, targetNode, grid):
    # gCost - distance from starting node
    # hCost - distance from target node
    #  fCost = gCost + hCost

    # openSet contains nodes that are candidates for examining
    openSet = []
    # closedSet contains nodes that have already been examined
    closedSet = set()

    # openSet.add(startNode)
    heappush(openSet, (startNode.distance, startNode))
    while openSet:
        curr = heappop(openSet)
        # curr.gCost = 0
        # curr.heuristicCost = 0
        curr.distance = 0
        neighbors = getNeighbors(cur, grid)
        closedSet.add(curr)
        curr.isVisited = True
        if curr == targetNode:
            return
        for neighbor in neighbors:
            if neighbor.isVisited:
                continue
            neighbor.gCost = curr.gCost + 1  # 1 is the distance between neighbor and curr node
            neighbor.heuristicCost = manhattanDistance(neighbor, targetNode)
            neighbor.distance = neighbor.gCost + neighbor.heuristicCost
            if neighbor not in openSet:
                openSet.add(neighbor)
                neighbor.prev = curr


def manhattanDistance(node, targetNode):
    # Use this heuristic when move only in 4 directions (left, right, up, down)
    return abs(node.row - targetNode.row) + abs(node.col - targetNode.col)


def euclideanDistance(startNode, endNode):
    # used when move in any direction
    return sqrt((startNode.row - endNode.row) ** 2 + (startNode.col - endNode.col) ** 2)


def getNeighbors(node, grid):
    neighbors = []
    row, col = node.row, node.col

    if col < len(grid[0]) - 1:
        neighbors.append(grid[row][col+1])
    if col > 0:
        neighbors.append(grid[row][col-1])
    if row > 0:
        neighbors.append(grid[row-1][col])
    if row < len(grid) - 1:
        neighbors.append(grid[row+1][col])

    return neighbors
