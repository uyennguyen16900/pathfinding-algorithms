from node import Node


def bfs(start, target, grid):
    startNode = Node(start[0], start[1])
    targetNode = Node(target[0], target[1])
    queue = []
    startNode.isVisited = True
    queue.append(startNode)
    while queue:
        curr = queue.pop(0)
        if curr == targetNode:
            return getPath(startNode, curr, grid)
        for neighbor in getNeighbors(curr, grid):
            if not neighbor.isVisited:
                neighbor.prev = curr
                neighbor.isVisisted = True
                queue.append(neighbor)


def getNeighbors(node, grid):
    neighbors = []

    for new_position in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        node_position = (
            node.row + new_position[0], node.col + new_position[1])
        #  within range and walkable
        print(node_position[0], node_position[1])
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


maze = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
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
print(bfs(start, end, maze))
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
