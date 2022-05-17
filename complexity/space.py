def sum_rec(n):
    """_summary_
    1 + 0
    2 + 1
    3 + 3
    4 + 6
    5 + 10
    = 15
    time complexity = O(n)
    space "" = O(n)
    """
    if n <= 0:
        return 0
    return n + sum(n-1)


def fibo(n):
    """
    0 1 1 2 3 5 8 13 21 .....
    fibo(1)+fibo(0)
    fibo(2) + 1  fibo(1) + fibo(0) fibo(1) + fibo(0)
    fibo(3) + fibo(2)  fibo(2) + fibo(1)
    fibo(4)+fibo(3)
    fibo(5)
    O(2^n)
    optimized with dynamic programming
    """
    if n <= 1:
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(5))