import time
import random

class Metrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

def insertion_sort(arr):
    metrics = Metrics()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            metrics.comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            metrics.swaps += 1
        arr[j + 1] = key
        metrics.swaps += 1
        if j >= 0:
            metrics.comparisons += 1
    return metrics

def measure_insertion_sort(arr):
    start_time = time.time()
    metrics = insertion_sort(arr)
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
            print(f'\nTestando Insertion Sort com {size} elementos, distribuição {distribution}:')
            arr_copy = arr.copy()
            execution_time, comparisons, swaps = measure_insertion_sort(arr_copy)
            print(f'Insertion Sort - Tempo: {execution_time:.2f} ms, Comparações: {comparisons}, Trocas: {swaps}')

if __name__ == "__main__":
    run_tests()
