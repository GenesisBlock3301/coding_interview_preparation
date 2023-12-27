package main

import "fmt"

type TreeNode struct {
	val   int
	left  *TreeNode
	right *TreeNode
}

func (node *TreeNode) String() string {
	return fmt.Sprintf("%d", node.val)
}

func NewNode(val int, left *TreeNode, right *TreeNode) *TreeNode {
	return &TreeNode{
		val:   val,
		left:  left,
		right: right,
	}
}

func InsertData(root *TreeNode, val int) {
	if root != nil {
		if val > root.val {
			if root.right == nil {
				root.right = NewNode(val, nil, nil)
			} else {
				InsertData(root.right, val)
			}
		} else if val < root.val {
			if root.left == nil {
				root.left = NewNode(val, nil, nil)
			} else {
				InsertData(root.left, val)
			}
		}
	}
}

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 1 {
		return &TreeNode{val: nums[0]}
	}
	if len(nums) == 0 {
		return nil
	}
	mid := int(len(nums) / 2)
	root := &TreeNode{val: nums[mid]}
	root.left = sortedArrayToBST(nums[:mid])
	root.right = sortedArrayToBST(nums[mid+1:])
	return root
}

func main() {
	root := NewNode(3, nil, nil)
	InsertData(root, 2)
	InsertData(root, 5)
	InsertData(root, 1)
	InsertData(root, 3)
	InsertData(root, 6)
	//
	//fmt.Println(root)
	//fmt.Println(root.left)
	//fmt.Println(root.right)
	//fmt.Println(root.left.left)
	//fmt.Println(root.left.right)
	//fmt.Println(root.right.right)
	//nums := []int{-10, -3, 0, 5, 9}
	//fmt.Println(sortedArrayToBST(nums).right)

}
