
class Graph(object):
    def __init__(self):
        self.adjacency = dict()
        self.nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
        else:
            print(f"{node} already exist in self.nodes")

    # adjacency list with unweighted node
    def add_edges(self, node1, node2):
        temp = list()
        if node1 in self.nodes and node2 in self.nodes:
            if node1 not in self.adjacency:
                temp.append(node2)
                self.adjacency[node1] = temp
            else:
                temp.extend(self.adjacency[node1])
                temp.append(node2)
                self.adjacency[node1] = temp
        else:
            print("Node doesn't exist.")

    # add adjacency weighted edge
    def add_weighted_edge(self, node1, node2, weight):
        temp = list()
        if node1 in self.nodes and node2 in self.nodes:
            if node1 not in self.adjacency:
                temp.append([node2, weight])
                self.adjacency[node1] = temp
            else:
                temp.extend(self.adjacency[node1])
                temp.append([node2, weight])
                self.adjacency[node1] = temp
        else:
            print(f"Node doesn't exist")


print("Unweighted Operation")
graph = Graph()
for i in range(0, 5):
    graph.add_node(i)

# print(self.nodes)
# add_edges(0, 1)
# add_edges(1, 2)
# add_edges(2, 3)
# add_edges(3, 4)
# add_edges(3, 0)
# add_edges(4, 0)
# print(self.adjacency)

print("Weighted operation")

graph.add_weighted_edge(0, 1, 2)
graph.add_weighted_edge(1, 2, 2)
graph.add_weighted_edge(2, 3, 4)
graph.add_weighted_edge(3, 0, 5)
graph.add_weighted_edge(3, 4, 3)
graph.add_weighted_edge(4, 0, 1)
print(graph.adjacency)