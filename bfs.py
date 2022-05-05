graph = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}

queue = []
visited = []
output = []


def bfs(graph, queue, visited, output, start_node):
    queue.append(start_node)
    visited.append(start_node)
    iteration = 0
    while queue:
        iteration = iteration + 1
        print("<------------------------ITERATION", iteration, "------------------------>")
        print("Queue        => ", queue)
        print("Visited      => ", visited)
        m = queue.pop(0)
        # print("\n", m)
        output.append(m)
        print("Output       => ", output)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return output


print(type(graph))
print(bfs(graph, queue, visited, output, "5"))
