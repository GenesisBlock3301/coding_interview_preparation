# https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords( s: str) -> str:
    arr = [x for x in s.split(" ") if x]
    return " ".join(arr[::-1])


s = "the sky is blue"
s = "  hello world  "
print(reverseWords(s))