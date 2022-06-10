# https://leetcode.com/problems/linked-list-cycle/


from curses import flash


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class LinkList:
    def __init__(self) -> None:
        self.head = None

    def cycle_check(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
    def cycle_check_medium(self, head):
        s = set()
        temp = head
        c = 0
        while temp:
            if temp in s:
                return f"tail connects to node index {c}"
            c+=1
            s.add(temp)
            temp = temp.next
        return "no cycle"

    def cycle_check2(self, head):
        s = set()
        temp = head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

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
arr = [3]
link_list.insert_list(arr)
print(link_list.cycle_check(link_list.head))
print(link_list.cycle_check2(link_list.head))
print(link_list.cycle_check_medium(link_list.head))
print(link_list)
