# A* Algorithm

'''
Heuristic function
f(n) = h(n) + g(n)
g(n) : Actual cost path from the start node to the current node.
h(n) : Actual cost path from the current node the goal node

Process:

-- Initialization
1. Create two sets, one is open_set and another is closed_set
2. Create another set called g
3. Create a third set called parents.
4. Distance from start node to itself is always zero (g[start_node] = 0)
5. Parents of start_node is always itself (parents[start_node] = start_node)

-- Calculation
1. In a while loop, check condition whether len(open_set) > 0
2. If so, set a variable n set to None. This will be the current node.
3. For each v, check if f(n) > f(v). If so, set the value of n = v (Set n = v if n is None)
4. Skip if n equals to the end_node or we have reached the end of the graph.
5. Else get the set of the node m and its edge weight.
6. If the node m is not in both open & closed set, then add the node to the open set.
7. Set the parent node of m to n.
8. Set g(m) = g(n) + weight.
9. If m is in the open_set, compare g(m) and g(n) + weight
10. Set the parent node of m to n
11. If the node m is in closed_set, set the node to open set.
12. If the node n is not updated, return no path.
13. If the end node is reached, unpack all the keys of the parent dict.
14. Append the unpacked nodes to the path array.
15. Reverse the path array.
16. Return the path.
17. If path is not found, return no path found.
'''


# start_node = '0'
# end_node = '8'


def a_star(start_node, end_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}  # Store distance from start node.
    parents = {}  # Parents contain an adjacent map of all nodes.

    # Distance of start node from itself is zero
    g[start_node] = 0
    parents[start_node] = start_node

    print("OPEN -> ", open_set)
    print("CLOSED -> ", closed_set)
    while len(open_set) > 0:
        n = None

        # Node with the lowest f() is found.
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == end_node or Graph_node[n] == None:
            pass
        else:
            for (m, weight) in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print("Path doesn't exist")
            return None

        if n == end_node:
            path = []
            print("Parents", parents)
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print(f"Path found {path}")
            print("OPEN -> ", open_set)
            print("CLOSED -> ", closed_set)
            return path

        open_set.remove(n)
        closed_set.add(n)
        print("OPEN -> ", open_set)
        print("CLOSED -> ", closed_set)
    print("Path doesn't exist!")
    return None


def get_neighbours(v):
    if v in Graph_node:
        return Graph_node[v]
    else:
        return None


def heuristic(n):
    h_dist = {
        'A': 11,
        'B': 2,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }

    return h_dist[n]


Graph_node = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 3)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

a_star('A', 'G')
