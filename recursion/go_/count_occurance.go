// Count the number of occurrences of a given element in an array.
package main

import "fmt"

func CountOccurrence(index int, arr []int, elements map[int]int) map[int]int {
	if index >= len(arr) {
		return elements
	}
	elements[arr[index]]++
	return CountOccurrence(index+1, arr, elements)
}
func main() {
	elements := make(map[int]int)
	i := 0
	fmt.Println(CountOccurrence(i, []int{1, 2, 3, 2}, elements))
}
