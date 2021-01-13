from node import Node


def dfs(start, target, grid):
    startNode = Node(start[0], start[1])
    targetNode = Node(target[0], target[1])

    stack = []
    startNode.isVisited = True
    stack.append(startNode)
    visited = set()
    visited.add((startNode.row, startNode.col))
    while stack:
        curr = stack.pop()
        if curr == targetNode:
            return getPath(startNode, curr, grid)
        for neighbor in getNeighbors(curr, grid):
            if (neighbor.row, neighbor.col) not in visited:
                visited.add((neighbor.row, neighbor.col))
                neighbor.prev = curr
                stack.append(neighbor)

        # return ([(stack[i].row, stack[i].col) for i in range(len(stack))])


def getNeighbors(node, grid):
    neighbors = []

    for new_position in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
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


# maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# start = (1, 1)
# end = (9, 9)

# print(dfs(start, end, maze))
# print(maze)
