package main

import "fmt"

func MergeSort(arr []int) []int {
	if len(arr) == 1 {
		return arr
	}
	mid := int(len(arr) / 2)
	left := MergeSort(arr[:mid])
	right := MergeSort(arr[mid:])
	return Merge(left, right)
}
func Merge(left []int, right []int) []int {
	var MergeList []int
	l1 := len(left)
	l2 := len(right)
	i := 0
	j := 0

	for i < l1 && j < l2 {
		if left[i] < right[j] {
			MergeList = append(MergeList, left[i])
			i++
		} else {
			MergeList = append(MergeList, right[i])
			j++
		}
	}
	if i < l1 {
		MergeList = append(MergeList, left[i:]...)
	} else if j < l2 {
		MergeList = append(MergeList, right[j:]...)
	}
	return MergeList
}
func main() {
	arr := []int{5, 3, 2, 1}
	fmt.Println(MergeSort(arr))
}
