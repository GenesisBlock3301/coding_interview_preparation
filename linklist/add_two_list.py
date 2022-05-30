#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = self.return_list(l1)
        arr2 = self.return_list(l2)
        add = [int(x) for x in str(int("".join(arr1)[::-1]) + int("".join(arr2)[::-1]))[::-1]]
        head = self.create_link(add)
        return head
    
    def return_list(self,head):
        temp = head
        arr = []
        while temp.next is not None:
            arr.append(str(temp.val))
            temp = temp.next
        arr.append(str(temp.val))
        return arr
        
    # create link list
    def create_link(self,elements):
        head = ListNode(elements[0])
        for element in elements[1:]:
            tem = head
            while tem.next is not None:
                tem = tem.next
            tem.next = ListNode(element)
        return head