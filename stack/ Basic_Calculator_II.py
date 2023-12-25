# https://leetcode.com/problems/basic-calculator-ii/
def basic_cal(_s):
    operator = "+"
    stack = []
    num = 0
    _s = _s.strip()
    c = 0
    for i in _s:
        if i.isdigit():
            num = num*10+int(i)
        if i in "+-*/" or c == len(_s)-1:
            if operator == "+":
                stack.append(num)
            elif operator == "-":
                stack.append(-num)
            elif operator == "/":
                v1 = stack.pop()
                stack.append(int(v1/num))
            elif operator == "*":
                v1 = stack.pop()
                stack.append(v1*num)
            operator = i
            num = 0
        c += 1
    return sum(stack)


# s = "30+55/22"
# s = " 3+5 / 2+"
s = "3+4"
print(basic_cal(s))
