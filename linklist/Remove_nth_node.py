
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    @staticmethod
    def removeNthFromEnd(head, n):
        if not head:
            return head
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
