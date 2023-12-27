class Solution:
    def finalString(self, s: str) -> str:
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == 'i':
                arr[:i] = arr[:i][::-1]
        return "".join([x for x in arr if x != 'i'])

    def finalString2(self, s: str) -> str:
        arr = []
        for i in s:
            if i == 'i':
                arr = arr[::-1]
            else:
                arr.append(i)
        return "".join(arr)


sol = Solution()
s = "poiinter"
print(sol.finalString2(s))



