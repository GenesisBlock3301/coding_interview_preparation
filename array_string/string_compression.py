
def compressed(string):
    c = 0
    str_arr = []
    for i in range(0, len(string)):
        c += 1
        if i+1 >= len(string) or string[i] != string[i+1]:
            str_arr.append(string[i])
            str_arr.append(str(c))
            c = 0
    return "".join(str_arr)


print(compressed("aaab"))
