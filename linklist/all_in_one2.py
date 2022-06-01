


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

    """ 
    1. Remove duplicate from from unsorted link list.
    """

    def remove_duplicate(self):
        s = set()
        if self.head is None:
            return self.head
        else:
            current_node = self.head
            previous_node = None
            while current_node is not None:
                if current_node.val in s:
                    previous_node.next = current_node.next
                else:
                    s.add(current_node.val)
                    previous_node = current_node
                current_node = current_node.next
    """
    input->1,2,3,3,4,4,5
    output -> 1,2,5

    """
    # def get_unique_list()

    def remove_all_duplicate(self):
        dummy = ListNode(next=self.head)
        itr = dummy
        current_node = self.head
        while current_node:
            isUnique = True
            while current_node.next and current_node.next.val == current_node.val:
                isUnique = False
                current_node = current_node.next
            
            if isUnique:
                itr.next = current_node
                itr = itr.next
            current_node = current_node.next
        itr.next = None
        self.head = dummy.next
        return self.head
        
    """ 
    2. Revers exiting linklist
    """

    def reverse(self):
        previous_node = None
        current_node = self.head
        next_node = None
        while current_node != None:
            # print("==",current_node.val)
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    """ 
    3. Return Kth to last. Implement an algorithm to find the Kth to last
    element of link list
    """

    def kth_to_last_iter(self, k):
        # print(head.val)
        current_node = self.head
        c = 1
        while current_node:
            if c == k:
                self.head = current_node
                self.head.next = current_node.next
                break
            c += 1
            current_node = current_node.next
        return self.head

    # def kth_to_last_rec(self,k):


link_list = LinkList()
arr = [1, 1, 1, 2, 3]
link_list.insert_list(arr)
# link_list.remove_duplicate()
# link_list.reverse()
# print(link_list)
# print(link_list.kth_to_last(2))
link_list.remove_all_duplicate()
print(link_list)
