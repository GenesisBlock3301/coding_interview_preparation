//# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

package main

import (
	"fmt"
	"sort"
)

func BinarySearch(nums []int, target int) bool {
	low, high := 0, len(nums)-1
	sort.Ints(nums)
	for low <= high {
		mid := int((low + high) / 2)
		if nums[mid] == target {
			return true
		} else if nums[mid] > target {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return false
}

func main() {

	//arr := []int{2, 5, 6, 0, 0, 1, 2}
	//target := 0
	//nums := []int{2, 5, 6, 0, 0, 1, 2}
	//target := 3
	//nums := []int{1, 0, 1, 1, 1}
	//target := 0
	nums := []int{1}
	target := 0
	fmt.Println(BinarySearch(nums, target))
}
