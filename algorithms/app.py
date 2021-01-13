from node import Node
from astar import astar
from bfs import bfs
from dijkstra import dijkstra
from dfs import dfs
from termcolor import colored


def move(start, target, grid, algorithm):
    if algorithm == "astar":
        return astar(start, target, grid)
    elif algorithm == "dijkstra":
        return dijkstra(start, target, grid)
    elif algorithm == "bfs":
        return bfs(start, target, grid)
    elif algorithm == "dfs":
        return dfs(start, target, grid)


if __name__ == "__main__":
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print('                PATHFINDING')
    print('-----------------------------------------------')
    for row in maze:
        print(''.join('{0} '.format(num) for num in row))

    startInp = input(colored(
        'Please enter a starting position (e.g. 2,1): ', 'cyan'))
    start = tuple(map(int, startInp.split(',')))
    endInput = input(colored(
        'Please enter an ending location (e.g. 2,1): ', 'cyan'))
    end = tuple(map(int, endInput.split(',')))
    algorithm = input(colored(
        'Please enter an algorithm (dfs, bfs, astar, dijkstra): ', 'cyan'))

    move(start, end, maze, algorithm)
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    for row in maze:
        print(''.join(colored('{0} '.format(num), 'blue') if num == '.' or num == 'S' or num == 'E' else ''.join(
            '{0} '.format(num)) for num in row))
