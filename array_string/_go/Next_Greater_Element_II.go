// https://leetcode.com/problems/next-greater-element-ii/

package main

import "fmt"

func left(index int, val int, left []int) int {
	start := 0
	end := index
	for i := start; i < end; i++ {
		if left[i] > val {
			return left[i]
		}
	}
	return -1
}
func right(index int, val int, right []int) (int, bool) {
	n := len(right)
	start := index + 1
	for i := start; i < n; i++ {
		if right[i] > val {
			return right[i], true
		}
	}
	return 0, false
}
func nextGreaterElements(nums []int) []int {
	n := len(nums)
	var arr []int
	for i := 0; i < n; i++ {
		r, rOk := right(i, nums[i], nums)
		if rOk {
			arr = append(arr, r)
		} else {
			l := left(i, nums[i], nums)
			arr = append(arr, l)
		}
	}
	return arr
}

func main() {
	//nums1 := []int{1, 2, 1}
	nums1 := []int{1, 2, 3, 4, 3}
	//nums1 := []int{1, 5, 3, 6, 8}
	//fmt.Println(nums1[0:3])
	fmt.Println(nextGreaterElements(nums1))
}
