# https://leetcode.com/problems/basic-calculator-ii/
def basic_cal(s):
    operator = "+"
    stack = []
    num = 0
    s = s.strip()
    c = 0
    for i in s:
        if i.isdigit():
            num = num*10+int(i)
        if i in "+-*/" or c == len(s)-1:
            if operator == "+":
                stack.append(num)
            elif operator == "-":
                stack.append(-num)
            elif operator == "/":
                v1 = stack.pop()
                # print(v1, num)
                # break
                stack.append(int(v1/num))
            elif operator == "*":
                v1 = stack.pop()
                stack.append(v1*num)
            operator = i
            num = 0
        c += 1
    return sum(stack)


# s = "3+5/2"
# s = " 3+5 / 2 "
s = "42"
print(basic_cal(s))
