class Graph:

    def __init__(self, size):
        self.adjacency_matrix = [[0 for _ in range(size)] for i in range(size)]
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertices")
        else:
            self.adjacency_matrix[v1][v2] = 1
            self.adjacency_matrix[v2][v1] = 1

        # Remove edges

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        # Print the matrix

    def print_matrix(self):
        for row in self.adjacency_matrix:
            for val in row:
                print('{:4}'.format(val), end=" "),
            print()

    def __len__(self):
        return self.size


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
print(g.adjacency_matrix, len(g))
g.print_matrix()
