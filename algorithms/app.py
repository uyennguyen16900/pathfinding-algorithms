from node import Node
from astar import astar
from bfs import bfs
from dijkstra import dijkstra


def move(startNode, targetNode, grid, algorithm):

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            new_node = Node(row, col)
            # grid[row][col] = Node(row, col)
            if grid[row][col] == "X":
                grid[row][col].isWall = True

    if algorithm == "astar":
        return astar(startNode, targetNode, grid)
    elif algorithm == "dijkstra":
        dijkstra(startNode, targetNode, grid)
    elif algorithm == "bfs":
        bfs(startNode, targetNode, grid)


def getPath(startNode, targetNode, grid):
    curr = targetNode
    # path = []
    while curr != startNode:
        curr = curr.prev
        grid[curr.row][curr.col] = '.'
    #     path.append((curr.row, curr.col))
    # return path


grid = ["XXXXXXXXXXXXXXXXXXXX",
        "      X    X       X",
        "X XXXXX XXXX XXX XXX",
        "X       X      X X X",
        "X X XXX XXXXXX X X X",
        "X X   X        X X X",
        "X XXX XXXXXX XXXXX X",
        "X XXX    X X X     X",
        "X    XXX       XXXXX",
        "XXXXX   XXXXXX     X",
        "X   XXX X X    X X X",
        "XXX XXX X X XXXX X X",
        "X     X X   XX X X X",
        "XXXXX     XXXX X XXX",
        "X     X XXX    X   X",
        "X XXXXX X XXXX XXX X",
        "X X     X  X X     X",
        "X X XXXXXX X XXXXX X",
        "X X                X",
        "XXXXXXXXXXXXXXXXXX X"]
# startNode = Node(1, 0, 0)
# targetNode = Node(19, 18, 0)

# move(startNode, targetNode, grid, astar)
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
end = (7, 6)


startNode = Node(start[0], start[1])
print(astar(start, end, maze))
print(startNode == astar(start, end, maze))
# targetNode = move(start, end, maze, astar)
# print(targetNode)
# getPath(startNode, targetNode, maze)
# print(path)
