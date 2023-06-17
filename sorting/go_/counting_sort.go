package main

import (
	"fmt"
	"sort"
)

// counting sort time complexity O(m+n)

func CountingSort(arr []int) []int {
	length := len(arr)
	Output := make([]int, length)
	sort.Ints(arr)
	MaxVal := arr[length-1]
	Count := make([]int, MaxVal+1)
	for _, val := range arr {
		Count[val]++
	}
	for i := 1; i < length; i++ {
		Count[i] += Count[i-1]
	}
	i := length - 1
	for i >= 0 {
		val := Count[arr[i]]
		fmt.Println(val, arr[i])
		Output[val-1] = arr[i]
		Count[arr[i]]--
		i--
	}
	return Output
}

func main() {
	arr := []int{4, 2, 2, 8, 3, 3, 1}
	fmt.Println(CountingSort(arr))
}
