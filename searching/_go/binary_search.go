package main

import "fmt"

func BinarySearch(arr []int, target int) bool {
	low, high := 0, len(arr)

	for low <= high {
		mid := int((low + high) / 2)
		if arr[mid] == target {
			return true
		} else if arr[mid] > target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return false
}

func main() {

	arr := []int{1, 2, 3, 4, 5, 6, 7, 8}
	fmt.Println(BinarySearch(arr, 5))
}
