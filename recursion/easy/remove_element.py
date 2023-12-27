# https://leetcode.com/problems/remove-linked-list-elements/
# https://leetcode.com/problems/delete-node-in-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


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

    """
    step 1: Check head exist or not
    step 2: Every node mark as a head node and it has next.
    step 3: if node.val == val jump to next node
    step 4: if not, just head.next link with next
    """

    def removeElements(self, head, val):
        # print(head.val)
        if not head:
            return None
        else:
            if head.val == val:
                return self.removeElements(head.next, val)
            else:
                head.next = self.removeElements(head.next, val)
                return head

    """
    1. No need to access head
    2. Just focus on specific node
    3. First take current node's next value for linking with node previous value.
    4. Replace current node.val with next node value.
    5. Replace current node.next with next node next value.
    """

    def deleteNode(self, node):
        after_node = node.next
        node.val = after_node.val
        node.next = after_node.next
        del after_node

    def append_to_tail(self, val):
        node = ListNode(val)
        # If linklist empty so head is none,
        # So put node in self.head.next.
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        return self.head

    def insert_list(self, arr):
        for element in arr:
            self.append_to_tail(element)
        return self.head


link_list = LinkList()
# arr = [1,2,6,3,4,5,6]
# val = 6

head = [4, 5, 1, 9]
node = 1
link_list.insert_list(head)
# link_list.removeElements(link_list.head,val)
link_list.deleteNode(head)
print(link_list)
