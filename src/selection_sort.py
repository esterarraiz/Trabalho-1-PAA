import time
import random

class Metrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

def selection_sort(arr):
    metrics = Metrics()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            metrics.comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            metrics.swaps += 1
    return metrics

def measure_selection_sort(arr):
    start_time = time.time()
    metrics = selection_sort(arr)
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

def run_tests_selection_sort():
    sizes = [1000, 10000, 50000, 100000]
    distributions = ['random', 'sorted', 'reversed']

    for size in sizes:
        for distribution in distributions:
            arr = generate_list(size, distribution)
            print(f'\nTestando Selection Sort com {size} elementos, distribuição {distribution}:')
            execution_time, comparisons, swaps = measure_selection_sort(arr)
            print(f'Tempo: {execution_time:.2f} ms, Comparações: {comparisons}, Trocas: {swaps}')

if __name__ == "__main__":
    run_tests_selection_sort()
