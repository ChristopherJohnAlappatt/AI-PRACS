graph = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}
visited = []
stack = []
output = []


def dfs(visited, stack, output, graph, start_node):
    print("WELCOME TO DFS PROGRAM")
    stack.append(start_node)
    visited.append(start_node)

    while stack:
        m = stack.pop()
        output.append(m)

        for neighbour in graph[m]:
            if neighbour not in visited :
                visited.append(neighbour)
                stack.append(neighbour)


if __name__ == '__main__':
    dfs(visited, stack, output, graph, "5")
    print(output)
