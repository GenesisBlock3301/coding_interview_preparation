# https://leetcode.com/problems/make-the-string-great/


def great_string(s):
    stack = []
    for i in s:
        if stack:
            if (ord(stack[-1]) != ord(i)) and (stack[-1].lower() == i.lower()):
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
            
    return "".join(stack)


# s = "leEeetcode"
# s = "abBAcC"
# s = "Pp"
s = 'Hvh'
print(great_string(s))
