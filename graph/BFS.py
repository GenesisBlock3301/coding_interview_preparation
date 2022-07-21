
def bfs(graph, source):
    visited = set()
    queue = list()
    queue.append(source)
    visited.add(source)
    while queue:
        vertex = queue.pop(0)
        print(f"{vertex}", end=" ")
        for n in graph[vertex]:
            if n not in visited:
                visited.add(n)
                queue.append(n)


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print("Following is Breadth First Traversal: ")
bfs(graph, 0)
