import time
import random

class SortMetrics:
    def __init__(self): 
        self.comparisons = 0
        self.swaps = 0

def heapify(arr, n, i, metrics):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    metrics.comparisons += 1
    if left < n and arr[left] > arr[largest]:
        largest = left

    metrics.comparisons += 1
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        metrics.swaps += 1
        heapify(arr, n, largest, metrics)

def heap_sort(arr, metrics):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, metrics)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        metrics.swaps += 1
        heapify(arr, i, 0, metrics)

def generate_test_arrays(size):
    ordered = list(range(size))
    reversed_ordered = list(range(size, 0, -1))
    random_array = random.sample(range(size), size)
    return ordered, reversed_ordered, random_array

def run_test(sort_function, array, metrics):
    start_time = time.time()
    sort_function(array.copy(), metrics)
    end_time = time.time()
    return (end_time - start_time) * 1000  

def test_heap_sort():
    sizes = [1000, 10000, 50000, 100000]
    for size in sizes:
        print(f"\nTamanho do array: {size}")
        ordered, reversed_ordered, random_array = generate_test_arrays(size)

        print("\n--- Heap Sort ---")
        for array, label in [(ordered, 'Ordenado'), (reversed_ordered, 'Inversamente Ordenado'), (random_array, 'Aleatório')]:
            metrics = SortMetrics()
            time_taken = run_test(heap_sort, array, metrics)
            print(f"Distribuição: {label}, Tempo: {time_taken:.3f}ms, Comparações: {metrics.comparisons}, Trocas: {metrics.swaps}")

test_heap_sort()
