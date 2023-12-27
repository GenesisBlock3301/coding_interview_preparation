# https://leetcode.com/problems/palindrome-linked-list


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class LinkList:
    def __init__(self) -> None:
        self.head = None
        self.first_half_head = None

    def __str__(self) -> str:
        nodes = []
        current_node = self.first_half_head
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
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        return self.head

    def insert_list(self, arr):
        for element in arr:
            self.append_to_tail(element)
        return self.head

    def checkPalindrome1(self, head):
        """
        space complexity O(1) time O(n) 
        """
        val = []
        current_node = head
        while current_node:
            val.append(current_node.val)
            current_node = current_node.next
        return val == val[::-1]

    def checkPalindrome2(self, head):
        """
        space complexity O(1) time O(n) 
        """
        c = 0
        current_node = head
        while current_node:
            current_node = current_node.next
            c += 1
        first_half_head = None
        second_half = None

        middle = c//2

        if middle % 2 == 0:
            middle = middle
        else:
            middle = middle - 1

        previous_node = None
        current_node = head
        next_node = None
        c = 0
        while current_node is not None:
            c += 1
            if c == middle:
                break
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        first_half_head = previous_node
        second_half = current_node if middle % 2 != 0 else current_node.next
        cur1 = first_half_head
        cur2 = second_half
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return first_half_head.val

    def reverse(self, head):
        previous_node = None
        current_node = head
        next_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


link_list = LinkList()
# arr = [1, 0, 1]
arr = [1, 2, 2, 1]
link_list.insert_list(arr)
# print(link_list.checkPalindrome(link_list.head))
print(link_list.checkPalindrome2(link_list.head))
# link_list.reverse(link_list.head)
# print(link_list)
