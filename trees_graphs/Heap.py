
def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return i//2


def is_max_heap(H):
    n = len(H) - 1

    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False
    return True


def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and heap[r] > heap[i]:
        largest = r
    if largest == i:
        return
    heap[i], heap[largest] = heap[largest], heap[i]
    max_heapify(heap, heap_size, largest)


def build_max_heap(heap):
    heap_size = len(heap) - 1
    for i in range(heap_size//2-1, -1, -1):
        max_heapify(heap, heap_size, i)


def heap_sort(heap):
    build_max_heap(heap)
    print("Max heap: ",heap)
    heap_size = len(heap) - 1
    for i in range(heap_size, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap_size -= 1
        max_heapify(heap, heap_size, 0)


if __name__ == "__main__":
    # H = [12, 7, 1, 3, 10, 17, 19, 2, 5]
    # print("Before building heap: ", H)
    # heap_sort(H)
    # print("After building heap: ",H)
    H = [1, 2, 3]
    max_heapify(H, 3, 0)
    print(H)