def singleNumber(A):
    singleElement = 0
    for i in A:
        singleElement ^= i
    return singleElement


# Example array
array = [4, 4, 5, 100, 5]

unique = singleNumber(array)
print("Unique value in the array:", unique)
