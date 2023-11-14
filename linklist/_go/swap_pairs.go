package main

type listNode struct {
	value int
	next  *listNode
}

func listNode_new(val int) *listNode {
	var node *listNode = new(listNode)
	node.value = val
	node.next = nil
	return node
}

func swapPairs(A *listNode) *listNode {
	dummy := listNode_new(0)
	dummy.next = A
	current := dummy
	for current.next != nil && current.next.next != nil {
		node1 := current.next
		node2 := current.next.next

		current.next = node2
		node1.next = node2.next
		node2.next = node1
		current = node1
	}
	return dummy.next
}
