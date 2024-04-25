package main

import "fmt"

func strStr(haystack string, needle string) int {
	i, j := 0, 0
	hL := len(haystack)
	nL := len(needle)
	ans := -1
	for i < hL {
		if haystack[i] == needle[j] {
			ans += 1
			if j >= nL {
				break
			}
			i++
			j++
		} else {
			j += 1
		}
	}
	return ans
}

func main() {
	haystack := "sadbutsad"
	needle := "sad"
	fmt.Println(strStr(haystack, needle))
}
