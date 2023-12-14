package main

import "fmt"

func isPalindrome(A string) int {
	var arr []int32
	for _, val := range A {
		if (val >= 48 && val <= 57) || (val >= 65 && val <= 90) || (val >= 97 && val <= 122) {
			if val >= 65 && val <= 90 {
				val += 32
				arr = append(arr, val)
			} else {
				arr = append(arr, val)
			}
		}
	}
	i, j := 0, len(arr)-1
	for i <= j {
		if arr[i] != arr[j] {
			return 0
		}
		i++
		j--
	}
	return 1
}

func main() {
	A := "A man, a plan, a canal: Panama"
	//A := "1a2"
	fmt.Println(isPalindrome(A))
}
