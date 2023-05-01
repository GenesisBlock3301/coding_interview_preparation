package main

import "fmt"

// Merge Time complexity O(n log n) and space O(n)

func Merge(a []int, b []int) []int {
	var MargeArr []int
	lenA, lenB := len(a), len(b)
	indexA, indexB := 0, 0
	for indexA < lenA && indexB < lenB {
		if a[indexA] < b[indexB] {
			MargeArr = append(MargeArr, a[indexA])
			indexA++
		} else {
			MargeArr = append(MargeArr, b[indexB])
			indexB++
		}
	}
	if indexA < lenA {
		MargeArr = append(MargeArr, a[indexA:]...)
	} else if indexB < lenB {
		MargeArr = append(MargeArr, b[indexB:]...)
	}
	return MargeArr
}

// this function complexity O(log n)

func MergeSort(arr []int) []int {
	var mid int
	if len(arr) <= 1 {
		return arr
	}
	mid = len(arr) / 2
	left := MergeSort(arr[:mid])
	right := MergeSort(arr[mid:])
	return Merge(left, right)
}
func main() {
	arr := []int{4, 3, 2, 1}
	fmt.Println(MergeSort(arr))
}
