graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


def DLS(start, goal, path, level, maxD):
    print('\nCurrent level-->', level)
    print('Goal node testing for', start)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        return path
    print('Goal node testing failed')
    if level == maxD:
        return False
    print('\nExpanding the current node', start)
    for child in graph[start]:
        if DLS(child, goal, path, level + 1, maxD):
            return path
        path.pop()
    return False


start = '5'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
result = DLS(start, goal, path, 0, maxD)
if (result):
    print("Path to goal node available")
    print("Path", path)
else:
    print("No path available for the goal node in given depth limit")
