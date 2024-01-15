def is_distination(destination):
    return destination == "Dhaka"


def DFS(graph, starting_point, visited=None):
    if visited is None:
        visited = list()
    if "Dhaka" in visited:
        return
    visited.append(starting_point)
    # print(starting_point)
    for next in graph[starting_point]:
        if next not in visited:
            if is_distination(next):
                visited.append(next)
                return True
            else:
                DFS(graph, next, visited)
    return visited


# second-shortest path problem.

graph = dict()
graph["Jamalpur"] = ["Mymensingh", "Tangail"]
graph["Mymensingh"] = ["Gazipur"]
graph["Dhaka"] = []
graph["Tangail"] = ["Dhaka"]
graph["Gazipur"] = ["Dhaka"]
print(DFS(graph, "Jamalpur"))
