def even_odd_addition(n):
    return even(n), odd(n)


def odd(n):
    if n < 0:
        return 0

    if n % 2 != 0:
        return n + odd(n - 1)
    return odd(n-1)


def even(n):
    if n < 0:
        return 0
    if n % 2 == 0:
        return n + even(n - 1)
    return even(n - 1)


print(even_odd_addition(5))
