package main

import "fmt"

func BubbleSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] > arr[j] {
				temp := arr[i]
				arr[i] = arr[j]
				arr[j] = temp
			}
		}
	}
	return arr
}

func main() {
	arr := []int{5, 3, 2, 1}
	fmt.Println(BubbleSort(arr))
}
