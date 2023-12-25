class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        length = len(A)
        G = [0] * length
        for i in range(1, length):
            closest = self.find_closest(A[:i], A[i])
            if closest != -1:
                G[i] = closest
            else:
                G[i] = -1
        G[0] = -1
        return G

    def find_closest(self, A, target):
        i = len(A) - 1
        while i >= 0:
            if A[i] < target:
                return A[i]
            i-=1
        return -1



s = Solution()
A = [4, 5, 2, 10, 8]
A = [34, 35, 27, 42, 5, 28, 39, 20, 28]
# A = [35, 27, 42]
A = [1]
print(s.prevSmaller(A))

# arr = [ 34, 35, 27]
# visited = [False] * len(arr)
# target = 42
# # arr = list(filter(lambda x: x < target, arr))
# a = []
# visited[0] = True
# visited[1] = True
# for i in range(len(arr)):
#     if arr[i] < target and not visited[i]:
#         a.append(arr[i])

# result = max(a) if a else -1
# print(result)  # This will output 45
