package main

import "fmt"

// Boyer-Moore Majority Vote Algorithm
func majorityElement2(A []int) int {
	majoriry := len(A) / 2
	hashMap := make(map[int]int)
	var _maxVal, element int
	for _, val := range A {
		hashMap[val]++
		if hashMap[val] > _maxVal {
			_maxVal = hashMap[val]
			element = val
		}
	}
	if _maxVal > majoriry {
		return element
	}
	return -1
}

func main() {
	nums := []int{3, 3, 4, 2, 4, 4, 2, 4, 4}
	result := majorityElement2(nums)
	fmt.Printf("The majority element is: %d\n", result)
}
