from os import nice


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class LinkList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        nodes = []
        current_node = self.head
        while current_node.next:
            nodes.append(str(current_node))
            current_node = current_node.next
        nodes.append(str(current_node))
        return ",".join(nodes)

    def append_to_tail(self, data):
        node = Node(data)
        # If linklist empty so head is none,
        # So put node in self.head.next.
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
        return self.head

    def insert_list(self, arr):
        for element in arr:
            self.append_to_tail(element)
        return self.head

    def remove_duplicate(self):
        s = set()
        if self.head is None:
            return self.head
        else:
            current_node = self.head
            previous_node = None
            while current_node is not None:
                if current_node.data in s:
                    previous_node.next = current_node.next
                else:
                    s.add(current_node.data)
                    previous_node = current_node
                current_node = current_node.next

    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node != None:
            current_node.next = previous_node
            previous_node = current_node
            # previous_node.next = current_node
            current_node = current_node.next
        self.head = previous_node
    
    def print_linklist(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next


link_list = LinkList()
link_list.insert_list([1, 2, 3, 4])
# link_list.remove_duplicate()
link_list.reverse()
print(link_list)
print(link_list.print_linklist())
