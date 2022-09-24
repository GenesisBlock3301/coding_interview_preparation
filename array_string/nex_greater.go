// # https://leetcode.com/problems/next-greater-element-i/

package main

import "fmt"

func findIndexVal(v int, nums2 []int) int {
	for index, val := range nums2 {
		if v == val {
			return index
		}
	}
	return -1
}
func findNextGreater(val int, index int, nums2 []int) int {
	n := len(nums2)
	for i := index + 1; i < n; i++ {
		if val < nums2[i] {
			return nums2[i]
		}
	}
	return -1
}
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	var arr []int
	for _, val := range nums1 {
		index := findIndexVal(val, nums2)
		ans := findNextGreater(val, index, nums2)
		arr = append(arr, ans)
	}
	return arr
}

func main() {
	nums1 := []int{4, 1, 2}
	nums2 := []int{1, 3, 4, 2}
	//nums1 := []int{2, 4}
	//nums2 := []int{1, 2, 3, 4}
	//nums1 := []int{1, 3, 5, 2, 4}
	//nums2 := []int{6, 5, 4, 3, 2, 1, 7}
	fmt.Println(nextGreaterElement(nums1, nums2))

}
