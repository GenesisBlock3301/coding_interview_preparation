class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        k2 = k + k
        if len(arr) < k:
            return "".join(arr[::-1])
        lower = 0
        i = 0
        while lower < len(arr):
            arr[lower:lower+k] = arr[lower:lower+k][::-1]
            lower += k2
            i += 1
        return "".join(arr)


s = "abcdef"
k = 2
sol = Solution()
print(sol.reverseStr(s, k))
