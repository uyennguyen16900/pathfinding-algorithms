from node import Node
from astar import astar
from bfs import bfs
from dijkstra import dijkstra


def move(startPosition, targetPosition, grid, algorithm):
    if algorithm == "astar":
        return astar(startNode, targetNode, grid)
    elif algorithm == "dijkstra":
        return dijkstra(startNode, targetNode, grid)
    elif algorithm == "bfs":
        return bfs(startNode, targetNode, grid)


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
print


startNode = Node(start[0], start[1])
print(astar(start, end, maze))
print(startNode == astar(start, end, maze))
# targetNode = move(start, end, maze, astar)
# print(targetNode)
# getPath(startNode, targetNode, maze)
# print(path)
