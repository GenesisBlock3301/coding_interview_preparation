
from asyncio import current_task


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class LinkList:
    def __init__(self) -> None:
        self.head = None

    
    """
    Write code to partition a linked list around a value x, such that all nodes less than
    all nodes less than x come from before all  nodes greater than or equal to x. If x is contain
    within the list, the values of x only need to be after the element less than x. The partition
    element x can appear anywhere in the "right partition"; it does not need to appear the left
    and right partition.
    """
    def partition(selfm ,head):
        pass
    
    """
    Implement an algorithm to delete a node in the middle(i.e, any node but the first and last
    node not necessary the exact middle) of singly link list, given only access to
    that node.
    input: a -> b -> c -> d -> e -> f, c
    output: a -> b -> d -> e -> f
    """

    def delete_middle_node(self, head, node):
        if head is None:
            return
        prev_node = None
        current_node = head
        if self.head.val == node:
            self.head = self.head.next
            return self.head
        while current_node:
            if current_node.val == node:
                break
            else:
                prev_node = current_node
                current_node = current_node.next
        prev_node.next = current_node.next

    def __str__(self) -> str:
        nodes = []
        current_node = self.head
        while current_node.next:
            nodes.append(str(current_node))
            current_node = current_node.next
        nodes.append(str(current_node))
        return ",".join(nodes)

    def append_to_tail(self, val):
        node = ListNode(val)
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


link_list = LinkList()
arr = [1, 2, 3]
link_list.insert_list(arr)
link_list.delete_middle_node(link_list.head, 3)
print(link_list)
