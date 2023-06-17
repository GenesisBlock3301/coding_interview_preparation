
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i+1,length):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

print(bubble_sort([6,5,4,2,2,1]))