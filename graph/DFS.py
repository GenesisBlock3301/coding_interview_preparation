

def DFS(graph, starting_point, visited=None):
    if visited is None:
        visited = list()
    visited.append(starting_point)
    print(starting_point)
    for next in graph[starting_point]:
        if next not in visited:
            DFS(graph, next, visited)
    return visited


graph = {
    1: set([2, 3]),
    2: set([4, 5]),
    3: set([]),
    4: set([]),
    5: set([])
}
print(DFS(graph, 1))
