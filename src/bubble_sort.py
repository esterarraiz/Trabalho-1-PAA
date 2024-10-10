import time
import random

class Metrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

def bubble_sort(arr):
    metrics = Metrics()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            metrics.comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                metrics.swaps += 1
    return metrics

def measure_bubble_sort(arr):
    start_time = time.time()
    metrics = bubble_sort(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Tempo em milissegundos
    return execution_time, metrics.comparisons, metrics.swaps

def generate_list(size, distribution):
    if distribution == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == 'sorted':
        return list(range(size))
    elif distribution == 'reversed':
        return list(range(size, 0, -1))

def run_tests_bubble_sort():
    sizes = [1000, 10000, 50000, 100000]
    distributions = ['random', 'sorted', 'reversed']

    for size in sizes:
        for distribution in distributions:
            arr = generate_list(size, distribution)
            print(f'\nTestando Bubble Sort com {size} elementos, distribuição {distribution}:')
            execution_time, comparisons, swaps = measure_bubble_sort(arr)
            print(f'Tempo: {execution_time:.2f} ms, Comparações: {comparisons}, Trocas: {swaps}')

if __name__ == "__main__":
    run_tests_bubble_sort()
