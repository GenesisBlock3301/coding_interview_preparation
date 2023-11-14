// https://leetcode.com/problems/jump-game/
package main

import (
	"fmt"
	"math"
)

func canJump(nums []int) bool {
	i, length, maxReach := 0, len(nums)-1, 0
	for i <= length && i <= maxReach {
		maxReach = int(math.Max(float64(maxReach), float64(i+nums[i])))
		i++
	}
	return i == len(nums)
}

func main() {
	//nums := []int{3, 2, 1, 0, 4}
	//nums := []int{2, 3, 1, 1, 4}
	nums := []int{2, 0}
	fmt.Println(canJump(nums))
}
