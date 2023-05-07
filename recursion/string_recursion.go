// Reverse a string recursively.
package main

import (
	"fmt"
	"strings"
)

func reverse(index int, str string, arr []string) []string {
	if index < 0 {
		return arr
	}
	arr = append(arr, string(str[index]))
	return reverse(index-1, str, arr)
}

func StringRecursion(str string) string {
	length := len(str)
	var arr []string
	return strings.Join(reverse(length-1, str, arr), "")
}

func main() {
	fmt.Println(StringRecursion("Nur Amin Sifat"))
}
