package main

import "fmt"

// Binary search's time complexity is Log(n) and space complexity O(n).
// but why, if we see in binary search every time the length of n become half than previous
// iteration. that means 8/2 = 4, 4/2 = 2, 2/2 = 1, that means 3 step to take complete iteration.
// if we take n = 256 then it will become 8, so easily we can compare it with log2(256) = 8 or log10(256)/log10(2)=8.

//but space complexity is O(1), because of in its runtime no additional space needed. it just use
// array for searching desire value.

// time -> O(log n) space -> O(1)

func BinarySearch1(array []int, target int) int {
	low, high := 0, len(array)-1
	var mid int
	for low <= high {
		mid = (low + high) / 2
		if array[mid] == target {
			return mid
		}
		if array[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

func CheckExistence(ans []int, value int) bool {
	for _, val := range ans {
		if value == val {
			return true
		}
	}
	return false
}

// BinarySearch2 time complexity O(log n) and space complexity same log(n) why?
// every recursive call occupied some space which is reduced like log(n)
func BinarySearch2(array []int, low int, high int, target int, ans []int) []int {
	var mid int
	for low <= high {
		mid = (low + high) / 2
		if array[mid] == target {
			if !CheckExistence(ans, mid) {
				ans = append(ans, mid)
				BinarySearch2(array, low, mid-1, target, ans)
				BinarySearch2(array, mid+1, high, target, ans)
			}
		}
		if array[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return ans
}

func main() {
	array := []int{1, 2, 3, 4, 5, 6}
	var ans []int
	fmt.Println(BinarySearch1(array, 6))
	fmt.Println(BinarySearch2(array, 0, len(array)-1, 6, ans))
}
