"""
A B-tree is a data structure used for efficiently storing and
retrieving large amounts of data. It is commonly used in database
systems and file systems, where it allows for fast access to data and efficient disk usage.
"""


class BTreeNode:
    """ B tree format"""

    def __init__(self, leaf=None):
        """A node has three property"""
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, degree):
        self.root = BTreeNode(True)
        # maximum number of child node
        self.degree = degree

    def insert_node(self, key):
        root = self.root
        if len(root.keys) == (2 * self.degree) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, key)
        else:
            self.insert_non_full(root, key)

    def split_child(self, node, i):
        degree = self.degree
        child = node.children[i]
        b_node = BTreeNode(node.leaf)
        node.children.insert(i, b_node)
        node.keys.insert(i, child.keys[degree - 1])
        b_node.keys = child.keys[degree:(2 * degree) - 1]
        child.keys = child.keys[0:degree - 1]
        if not child.leaf:
            b_node.children = child.children[degree:2 * degree]
            child.children = child.children[0, degree - 1]

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None, None)
            while i >= 0 and key[0] < node.keys[i][0]:
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key[0] < node.keys[i][0]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.degree) - 1:
                self.split_child(node, i)
                if key[0] > node.keys[i][0]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def search_key(self, key, node=None):
        if node is not None:
            i = 0
            while i < len(node.keys) and key > node.keys[i][0]:
                i += 1

            if i < len(node.keys) and key == node.keys[i][0]:
                return node, i
            elif node.leaf:
                return None
            else:
                return self.search_key(key, node.children[i])
        else:
            return self.search_key(key, self.root)
