def fact(n):
    if n == 0:
        return 1
    print(n)
    return n*fact(n-1)

print(fact(4))