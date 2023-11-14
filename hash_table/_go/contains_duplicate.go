// https://leetcode.com/problems/contains-duplicate/
package main

import "fmt"

func containsDuplicate(nums []int) bool {
	container := make(map[int]int)
	for _, val := range nums {
		container[val]++
	}
	for _, val := range container {
		if val > 1 {
			return true
		}
	}
	return false
}

func main() {
	nums := []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}
	fmt.Println(containsDuplicate(nums))
}
