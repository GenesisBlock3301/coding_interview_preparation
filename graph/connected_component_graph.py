# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/\

def connected_graph(graph):
    visited = list()
    conn_node = []
    for v in graph:
        if v not in visited:
            temp = []
            conn_node.append(helper(temp, v, visited))
    return conn_node


def helper(temp, v, visited, count=None):
    if count is None:
        count = 0
    visited.append(v)
    temp.append(v)
    count += 1
    for i in graph[v]:
        if i not in visited:
            temp = helper(temp, i, visited, count)
    return temp


graph = dict()
graph[1] = [0]
graph[2] = [3]
graph[3] = [4]
graph[4] = []
graph[0] = []
con_node = connected_graph(graph)
print(con_node)
