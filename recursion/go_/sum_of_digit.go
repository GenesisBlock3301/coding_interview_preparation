//Write a recursive function to calculate the sum of digits in a number.

package main

import "fmt"

func Helper(digit int) int {
	Sum := 0
	return SumOfDigit(digit, Sum)
}
func SumOfDigit(digit int, Sum int) int {
	if digit == 0 {
		return Sum
	}
	rem := digit % 10
	digit = digit / 10
	l := Sum + rem
	return SumOfDigit(digit, l)
}
func main() {
	fmt.Println(Helper(5050555))
}
