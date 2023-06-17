package main

import "fmt"

func SelectionSort(arr []int) []int {
	length := len(arr)
	for i := 0; i < length-1; i++ {
		IndexMin := i
		for j := i + 1; j < length; j++ {
			if arr[j] < arr[IndexMin] {
				IndexMin = j
			}
		}
		if IndexMin != i {
			temp := arr[i]
			arr[i] = arr[IndexMin]
			arr[IndexMin] = temp
		}
	}
	return arr
}

func main() {
	arr := []int{5, 2, 1, 3}
	fmt.Println(SelectionSort(arr))
}
