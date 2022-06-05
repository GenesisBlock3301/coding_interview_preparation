# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evalRPN(tokens) -> int:
    stack = []
    v1 = v2 = None
    for i in tokens:
        if i not in "+-*/":
            stack.append(int(i))
        else:
            v1 = stack.pop()
            v2 = stack.pop()
            if i == "+":
                result = v2+v1
                stack.append(result)
            elif i == "-":
                result = v2-v1
                stack.append(result)
            elif i == "*":
                result = v2*v1
                stack.append(result)
            elif i == "/":
                result = v2/v1
                stack.append(int(result))

    return stack[0]


# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))
