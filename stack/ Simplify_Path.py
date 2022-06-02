# https://leetcode.com/problems/simplify-path/

import os
# path = "/home//foo/"
# path = "/a/./b/../../c"


def real_path(path):
    stack = []

    p = path.split("/")
    for i in p:
        if i != "" and i != "." and i != "..":
            stack.append(i)
        elif i == "..":
            if stack:
                stack.pop()

    return "/"+"/".join(stack)


path = "/home//alone"
print(os.path.relpath(path))
print(real_path(path))
