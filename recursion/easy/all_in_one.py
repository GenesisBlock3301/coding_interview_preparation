# sum of digit of number
def sum_digit(num):
    if num == 0:
        return 0
    rem = num % 10
    num = int(num / 10)
    return rem + sum_digit(num)


print("Print sum of digit: ", sum_digit(142))


# Sum of first netral number
def sum_neutral_number(num):
    if num == 0:
        return 0
    return num + sum_neutral_number(num - 1)


sum = 0
# sum_neutral_number(5,sum)
print("Sum neutral number: ", sum_neutral_number(5))


def GCD(a, b):
    low = min(a, b)
    high = max(a, b)
    if low == 0:
        return high
    elif low == 1:
        return 1
    return GCD(low, high % low)


print(GCD(24, 12))
