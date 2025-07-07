def buildMaxHeap(arr, n):
    for i in range(n//2-1, -1, -1):
        maxHeapify(arr, i, n)

def maxHeapify(arr, i, heap_size):
    l = 2*i+1
    r = 2*i+2
    largest = i
    if l < heap_size and arr[l] > arr[largest]:
        largest = l

    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, heap_size)

def heapsort(arr):
    heap_size = len(arr)
    buildMaxHeap(arr, heap_size)
    for i in range(heap_size-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, 0, i)

    return arr

if __name__ == '__main__':
    A = [2,3,4,5,1]
    print(heapsort(A)[::-1])

