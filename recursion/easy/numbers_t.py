# write a functinion that takes in a number and prints it
# print first 5 numbers: 1,2,3,4,5

def printf(n):
    print(n)
    if n == 900:
        return 900
    printf(n + 1)


printf(1)
