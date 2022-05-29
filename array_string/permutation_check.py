"""
 Given two strings, write a method to decide if one is a permutation
 of the other.
"""
def permutation(s,t) -> bool:
    """Permutation means two different string but same length
    but they consist of same characters.
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def efficient_permutation(s,t) -> bool:
    """Permutation means two different string but same length
    but they consist of same characters.
    """
    if len(s) != len(t):
        return False
    letters = [0]*128
    s_array = list(s)
    for i in s_array:
        letters[ord(i)]+=1
    
    for j in t:
        letters[ord(j)]-=1
        if letters[ord(j)] < 0:
            return False
    return True
print(efficient_permutation("nass","sans"))