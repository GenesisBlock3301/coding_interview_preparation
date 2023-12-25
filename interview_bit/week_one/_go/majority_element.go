package main

import "fmt"

// Boyer-Moore Majority Vote Algorithm
func majorityElement(A []int) int {
	candidate := A[0]
	count := 1
	// Voting to candidate
	for i := 1; i < len(A); i++ {
		if A[i] == candidate {
			count++
		} else {
			count--
			if count == 0 {
				candidate = A[i]
				count = 1
			}
		}
	}
	count = 0
	for _, val := range A {
		if val == candidate {
			count++
		}
	}
	if count > len(A)/2 {
		return candidate
	}
	return -1
}

func main() {
	nums := []int{3, 3, 4, 2, 4, 4, 2, 4, 4}
	result := majorityElement(nums)
	fmt.Printf("The majority element is: %d\n", result)
}
