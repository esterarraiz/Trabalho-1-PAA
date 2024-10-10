import time
import random
import sys
sys.setrecursionlimit(10000)

class SortMetrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

def merge_sort(arr, metrics):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, metrics)
        merge_sort(right_half, metrics)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            metrics.comparisons += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                metrics.swaps += 1  
                i += 1
            else:
                arr[k] = right_half[j]
                metrics.swaps += 1  
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            metrics.swaps += 1 
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            metrics.swaps += 1  
            j += 1
            k += 1

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

def test_merge_sort():
    sizes = [1000, 10000, 50000, 100000]
    for size in sizes:
        print(f"\nTamanho do array: {size}")
        ordered, reversed_ordered, random_array = generate_test_arrays(size)

        print("\n--- Merge Sort ---")
        for array, label in [(ordered, 'Ordenado'), (reversed_ordered, 'Inversamente Ordenado'), (random_array, 'Aleatório')]:
            metrics = SortMetrics()
            time_taken = run_test(merge_sort, array, metrics)
            print(f"Distribuição: {label}, Tempo: {time_taken:.3f}ms, Comparações: {metrics.comparisons}, Trocas: {metrics.swaps}")

test_merge_sort()
