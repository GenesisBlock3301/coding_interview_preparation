package main

import "fmt"

func getRow(A int) []int {
	var arr [][]int
	for i := 1; i <= A+1; i++ {
		temp := make([]int, i)
		arr = append(arr, temp)
	}
	for i := 0; i < len(arr); i++ {
		arr[i][0] = 1
		arr[i][len(arr[i])-1] = 1
	}

	for row := 2; row < len(arr); row++ {
		i := 1
		for x := 1; x < len(arr[row-1]); x++ {
			arr[row][i] = arr[row-1][x-1] + arr[row-1][x]
			i++
		}
	}
	return arr[A]
}

func main() {
	fmt.Println(getRow(3))
	//arr := []int{1, 2, 3, 4, 5}
	//fmt.Println(arr[len(arr)-1])
}
