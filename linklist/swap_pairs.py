class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(A):
    dummy = ListNode(0)
    dummy.next = A
    current = dummy
    while current.next and current.next.next:
        node1 = current.next
        node2 = current.next.next

        current.next = node2
        node1.next = node2.next
        node2.next = node1

        current = node1

    return dummy.next

# Example usage:
# Create linked list
# For Input 1: A = 1 -> 2 -> 3 -> 4
# For Input 2: A = 7 -> 2 -> 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head2 = ListNode(7, ListNode(2, ListNode(1)))

# Call the function to swap pairs
result1 = swapPairs(head1)
result2 = swapPairs(head2)

# Print the results
while result1:
    print(result1.val, end=" -> ")
    result1 = result1.next
print("None")

while result2:
    print(result2.val, end=" -> ")
    result2 = result2.next
print("None")
