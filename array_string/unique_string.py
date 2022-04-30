# Bad practice

def is_unique_string(string): 
    """Find Time and space complexity
    then optimize that code, mind it argument and
    return type wont change, just change logic

    Args:
        string (_type_): Argument pass must string

    Returns:
        _type_: Return type must bool
    
    """
    dic = {}
    for i in string:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    for j in dic.values():
        if  j > 1:
            return False
    return True

print(is_unique_string("Sifatt"))
# 
# Good practice
def is_unique(string):
    """_summary_

    Args:
        string (_type_): _description_
    """ 
    if len(string) > 128: return False
    char_set = [0]*128
    for k in string:
        char_set[ord(k)]+=1
        if char_set[ord(k)] > 1:
            return False
    return True

print(is_unique("Sifat"))