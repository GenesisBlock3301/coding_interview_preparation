
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

    def prepend_head(self, data):
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

    def delete_element(self, data):
        current_node = self.head
        if self.head.data == data:
            self.head = self.head.next
        else:
            """
            1->2->3->4 DELETE 3
            """
            previous_node = None
            while current_node.next != None:
                if current_node.data == data:
                    break
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = current_node.next

    def insert_list(self, arr):
        for element in arr:
            self.append_to_tail(element)
        return self.head

    def swapPairs(self, head):
        """
         input: 1 2 3 4
         output: 2 1 4 3
        """
        if not head or not head.next:
            return head

        temp_next_pair = head.next.next
        temp_head = head
        head = head.next
        head.next = temp_head
        head.next.next = self.swapPairs(temp_next_pair)
        return head


link_list = LinkList()
# link_list.append_to_tail(2)
# link_list.append_to_tail(3)
# link_list.append_to_tail(4)
# link_list.prepend_head(1)
link_list.insert_list([1, 2, 3, 4])
# link_list.delete_element(4)
link_list.swapPairs(link_list.head)
print(link_list)
