# Análise Empírica de Algoritmos de Ordenação

Este repositório contém o código e o relatório para o trabalho de análise empírica de algoritmos de ordenação, desenvolvido para o curso de Ciência da Computação da UFT.

## Objetivo
O objetivo deste projeto é comparar o desempenho de seis algoritmos de ordenação, tanto em termos teóricos quanto práticos. Os algoritmos analisados são:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

## As métricas avaliadas incluem:

- Tempo de execução (medido em milissegundos)
- Número de comparações
- Número de trocas

## Estrutura do Repositório
- `src/`: Contém as implementações dos algoritmos de ordenação.
- `results/`: Resultados dos testes empíricos (tabelas e gráficos).
- `report/`: Relatório em LaTeX desenvolvido com UFTex.
- `README.md`: Este arquivo.

## Algoritmos Implementados
Cada algoritmo foi implementado em Python com a medição de:

- Tempo de execução
- Comparações realizadas
- Trocas realizadas

### Algoritmos Disponíveis:
- **Bubble Sort**: Implementação do Bubble Sort
- **Selection Sort**: Implementação do Selection Sort
- **Insertion Sort**: Implementação do Insertion Sort
- **Merge Sort**: Implementação do Merge Sort
- **Quick Sort**: Implementação do Quick Sort
- **Heap Sort**: Implementação do Heap Sort

## Metodologia
O experimento envolve a execução de cada algoritmo com listas de tamanhos:

- 1.000
- 10.000
- 50.000
- 100.000

## Distribuições das Listas:

- Ordenadas
- Inversamente Ordenadas
- Aleatórias

Os resultados são apresentados em tabelas e gráficos, comparando o desempenho de cada algoritmo.
