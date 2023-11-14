package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func NewListNode(val int) *ListNode {
	return &ListNode{
		Val:  val,
		Next: nil,
	}
}

func CreateLinkList(elements []int) *ListNode {
	head := NewListNode(elements[0])

	for _, element := range elements[1:] {
		tem := head
		for tem.Next != nil {
			tem = tem.Next
		}
		tem.Next = NewListNode(element)
	}
	return head
}

//func makeArray(head *ListNode) []int {
//	if head == nil {
//		return []int{}
//	}
//	var arr []int
//	tem := head
//	for tem != nil {
//		arr = append(arr, tem.Val)
//		tem = tem.Next
//	}
//	return arr
//}

func sortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

}

func main() {
	elements := []int{4, 2, 1, 3}
	head := CreateLinkList(elements)
	head1 := sortList(head)
	fmt.Println(head1.Next.Val)
}
