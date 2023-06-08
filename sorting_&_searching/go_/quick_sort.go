package main

func LeftRightValue(arr []int) []int {

}

func QuickSort(arr []int) []int {
	if len(arr) == 1 {
		return arr
	}
	pivot := arr[0]
	var LeftArray, RightArray []int
	for _, val := range arr {
		if val <= pivot {
			LeftArray = append(LeftArray, val)
		} else {
			RightArray = append(RightArray, val)
		}
	}
	return QuickSort(LeftArray)
}
