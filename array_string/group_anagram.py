# https://leetcode.com/problems/group-anagrams/

def find_anagram(strs):
    dic = dict()
    for v in strs:
        if dic.get("".join(sorted(v)), False):
            dic["".join(sorted(v))].append(v)
        else:
            dic["".join(sorted(v))] = list()
            dic["".join(sorted(v))].append(v)
    return list(dic.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(find_anagram(strs))
