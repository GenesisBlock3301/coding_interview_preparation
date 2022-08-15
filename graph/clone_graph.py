# https://leetcode.com/problems/clone-graph/
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        n = " ".join([str(x) for x in self.neighbors])
        return f"{self.val} -- {n}"


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        hash_map = dict()
        hash_map[node.val] = Node(node.val, [])
        self.helper(node, hash_map)
        return hash_map[node.val]

    def helper(self, node, hash_map=None):
        for nei in node.neighbors:
            if not nei.val in hash_map:
                hash_map[nei.val] = Node(nei.val, [])
                self.helper(nei, hash_map)
            hash_map[node.val].neighbors.append(hash_map[nei.val])


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
nodes = []
for i, val in enumerate(adjList):
    nodes.append(Node(i+1, val))
print(nodes[1])
s = Solution()
print(s.cloneGraph(nodes[0]))

