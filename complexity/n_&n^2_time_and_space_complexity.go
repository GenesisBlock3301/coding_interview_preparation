package main

import "fmt"

// Time and space complexity is O(n).

func SimpleIteration1(arr1 []int) []int {
	var arr2 []int
	for _, val := range arr1 {
		arr2 = append(arr2, val)
	}
	return arr2
}

// SimpleIteration2 time and space complexity O(n^2)

func SimpleIteration2(n int) [][]int {
	var arr2 [][]int
	for i := 0; i < n; i++ {
		var row []int
		for j := 0; j < n; j++ {
			row = append(row, j)
		}
		arr2 = append(arr2, row)
	}
	return arr2
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	fmt.Println(SimpleIteration1(arr))
	fmt.Println(SimpleIteration2(10))
}
