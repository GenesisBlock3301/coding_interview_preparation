# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
from collections import OrderedDict


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        hash_map = OrderedDict()
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        return self.__make_map_to_string(hash_map, k)

    @staticmethod
    def __make_map_to_string(hash_map: OrderedDict, _k: int) -> str:
        filtered_val = list()
        for key, value in hash_map.items():
            if value % _k != 0:
                filtered_val.append((key, value % _k))
        return ''.join(char*count for char, count in filtered_val)


obj = Solution()
s = "deeedbbcccbdaa"
k = 3
# s = "abcd"
# k = 2
# s = "pbbcggttciiippooaais"
# k = 2
s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"
k = 4
print(obj.removeDuplicates(s, k))

"yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"