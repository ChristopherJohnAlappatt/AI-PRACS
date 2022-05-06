graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


def BFS(start, goal, path, level, graph):
    print('\nCurrent level-->', level)
    print('Goal node testing for', start)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        print("GOAL NODE FOUND AT LEVEL ->  ", level)
        exit(0)
        return False
    print('\nExpanding the current node', start)
    for child in graph[start]:
        if BFS(child, goal, path, level + 1, graph):
            return path, level
        path.pop()
    return False


start = '5'
goal = input('Enter the goal node:-')
path = list()
result, level = BFS(start, goal, path, 0, graph)
if result:
    print("Path to goal node available")
    print("Path", path)
    print("Level", level)

else:
    print("No path available for the goal node in given depth limit")
