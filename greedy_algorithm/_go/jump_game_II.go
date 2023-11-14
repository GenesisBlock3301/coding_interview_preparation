package main

import "math"

func jump(nums []int) int {
	i, curr, next, length, ans := 0, -1, 0, len(nums)-1, 0
	for next < length {
		if i > curr {
			ans++
			curr = next
		}
		next = int(math.Max(float64(next), float64(i+nums[i])))

	}
	return ans
}
func main() {

}
