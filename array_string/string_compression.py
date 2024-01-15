"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become 
smaller than the original string, you method should return the original string. You can assume
the string has only uppercase and lowercase letters.
"""


def compressed(string):
    c = 0
    str_arr = []
    for i in range(0, len(string)):
        c += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            str_arr.append(string[i])
            str_arr.append(str(c))
            c = 0
    return "".join(str_arr)


print(compressed("aaab"))
