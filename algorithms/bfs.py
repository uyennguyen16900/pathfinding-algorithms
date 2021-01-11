def bfs(startNode, targetNode, grid):
    queue = []
    startNode.isVisited = True
    queue.append(startNode)
    while queue:
        curr = queue.pop(0)
        if curr == targetNode:
            return
        for neighbor in getNeighbors(curr, grid):
            neighbor.prev = curr
            neighbor.isVisisted = True
            queue.append(new_node)


def isValid(node, grid):
    row, col = node.row, node.col
    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 0 and not node.isVisited:
        return True
    else:
        return False


def getNeighbors(node, grid):
    neighbors = []

    for new_position in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        node_position = (
            node.row + new_position[0], node.col + new_position[1])
        #  within range and walkable
        if node_position[0] < len(grid) and node_position[0] >= 0 and node_position[1] >= 0 and node_position[1] < len(grid) and grid[node_position[0]][new_position[1]] == 0 and not node.isVisited:
            neighbors.append(Node(new_position[0], new_position[1]))

    return neighbors
