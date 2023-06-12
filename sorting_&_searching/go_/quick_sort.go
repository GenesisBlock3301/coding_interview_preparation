package main

import "fmt"

func QuickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	pivot := arr[0]
	var LeftArray, RightArray []int
	for _, val := range arr[1:] {
		if val <= pivot {
			LeftArray = append(LeftArray, val)
		} else {
			RightArray = append(RightArray, val)
		}
	}
	return append(append(QuickSort(LeftArray), pivot), QuickSort(RightArray)...)
}

func main() {
	b := []int{9, 7, 10, 8, 9}
	fmt.Println(QuickSort(b))
}
