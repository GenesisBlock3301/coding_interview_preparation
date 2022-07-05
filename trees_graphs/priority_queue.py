

def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return i//2


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


def get_maximum(heap):
    return heap[0]


def extract_maximum(heap, heap_size):
    max_item = heap[0]
    heap[0] = heap[heap_size]
    max_heapify(heap, heap_size, 1)
    return max_item

                                                                                                                                                                                                                                     