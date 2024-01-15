# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len, w2_len = len(word1), len(word2)
        arr = [''] * w1_len + [''] * w2_len
        modified_word = word1[:w2_len] if w1_len > w2_len else word2[:w1_len]
        length = len(modified_word) + len(word2) if w1_len > w2_len else len(word1) + len(modified_word)
        i, j, k = 0, 0, 0
        while k < length and (i < len(modified_word) or j < len(word2)):
            if k % 2 == 0:
                arr[k] = word1[i]
                i += 1
            else:
                arr[k] = word2[j]
                j += 1
            k += 1
        return "".join(arr+list(word1[i:] if w1_len > w2_len else word2[j:]))

    def mergeAlternately2(self, word1: str, word2: str) -> str:
        w1_len, w2_len = len(word1), len(word2)
        i, j = 0, 0
        arr = list()
        while i < w1_len and j < w2_len:
            arr.append(word1[i])
            arr.append(word2[j])
            i += 1
            j += 1

        while i < w1_len:
            arr.append(word1[i])
            i += 1

        while j < w2_len:
            arr.append(word2[j])
            j += 1

        return "".join(arr)


s = Solution()
word1 = "abcd"
word2 = "pq"

# word1 = "ab"
# word2 = "pqrs"
print(s.mergeAlternately2(word1, word2))