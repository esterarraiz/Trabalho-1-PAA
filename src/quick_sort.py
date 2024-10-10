import time
import random

class Metrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid] 
    return arr[high]

def quick_sort(arr, low, high, metrics):
    if low < high:
        pivot = partition(arr, low, high, metrics)
        quick_sort(arr, low, pivot - 1, metrics)
        quick_sort(arr, pivot + 1, high, metrics)

def partition(arr, low, high, metrics):
    pivot = median_of_three(arr, low, high)
    i = low - 1
    for j in range(low, high):
        metrics.comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            metrics.swaps += 1  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    metrics.swaps += 1  
    return i + 1

def measure_quick_sort(arr):
    metrics = Metrics()
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1, metrics)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    return execution_time, metrics.comparisons, metrics.swaps

def generate_list(size, distribution):
    if distribution == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == 'sorted':
        return list(range(size))
    elif distribution == 'reversed':
        return list(range(size, 0, -1))

def run_tests():
    sizes = [1000, 10000, 50000, 100000]
    distributions = ['random', 'sorted', 'reversed']

    for size in sizes:
        for distribution in distributions:
            arr = generate_list(size, distribution)
            print(f'\nTestando Quick Sort com {size} elementos, distribuição {distribution}:')
            arr_copy = arr.copy()
            execution_time, comparisons, swaps = measure_quick_sort(arr_copy)
            print(f'Quick Sort - Tempo: {execution_time:.2f} ms, Comparações: {comparisons}, Trocas: {swaps}')

if __name__ == "__main__":
    run_tests()