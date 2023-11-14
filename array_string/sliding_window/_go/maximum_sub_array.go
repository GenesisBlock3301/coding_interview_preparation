package main

import "fmt"

func maxSubArray(nums []int) int {
	mxSum := nums[0]
	start := 0
	currentSum := nums[0]
	result := []int{nums[0]}
	for end := 1; end < len(nums); end++ {
		if nums[end] > currentSum+nums[end] {
			currentSum = nums[end]
			start = end
		} else {
			currentSum += nums[end]
		}
		if currentSum > mxSum {
			mxSum = currentSum
			result = nums[start : end+1]
		}
	}
	return Sum(result)
}

func Sum(result []int) int {
	val := 0
	for _, v := range result {
		val += v
	}
	return val
}
func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println(maxSubArray(nums))
}
