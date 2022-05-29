


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

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

    def prepend_head(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        self.head.next = temp
        return self.head

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
    
    def delete_element(self,data):
        current_node = self.head
        if self.head.data == data:
            self.head = self.head.next
        previous_node = None
        while current_node.next != None:
            if current_node.data == data:
                break
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next

    def insert_list(self,arr):
        for element in arr:
            self.append_to_tail(element)
            



link_list = LinkList()
link_list.append_to_tail(2)
link_list.append_to_tail(3)
link_list.append_to_tail(4)
link_list.prepend_head(1)
link_list.insert_list([11,22,33,44,55,66])
link_list.delete_element(4)
print(link_list)
