

def divide(dividend, divisor):
    # print("start")
    # operator = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    # dividend = abs(dividend)
    # divisor = abs(divisor)
    # mul = 0
    # while dividend > divisor:
    #     dividend -= divisor
    #     mul += 1
    #     if operator > 0:
    #         mul = min(mul, 2**31-1)

    #     else:
    #         mul = max(mul, -2**31)

    # return mul*operator
    result = int(dividend / divisor)
    if result > (2**31)-1:
        return (2**31)-1
    elif result < (-2)**31:
        return (-2)**31
    else:
        return result


print(divide(-2147483648, -1))
