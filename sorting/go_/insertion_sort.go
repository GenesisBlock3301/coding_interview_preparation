package main

import "fmt"

func InsertionSort(nums []int) []int {
	length := len(nums)
	for i := 1; i < length; i++ {
		item := nums[i]
		j := i - 1
		for j >= 0 && nums[j] > item {
			nums[j+1] = nums[j]
			j--
			nums[j+1] = item
		}
	}
	return nums
}

func main() {
	arr := []int{5, 3, 2, 1}
	fmt.Println(InsertionSort(arr))
}
