# MSCS532_Assignment5: Deterministic vs. Randomized Quicksort

This project compares the performance of deterministic and randomized quicksort algorithms.

## Reports

- [Deterministic Quicksort Analysis](deterministic_quick_sort.md)
This report analyzes the deterministic Quicksort algorithm, which consistently selects the last element as the pivot. It details the time and space complexity, highlighting that the worst-case O(n^2) complexity occurs with sorted or reverse-sorted input, while the best and average cases are O(n log n).

- [Randomized Quicksort Analysis](randomized_quick_sort.md)
This report explains Randomized Quicksort, which randomizes pivot selection to overcome the weaknesses of the deterministic version. By choosing a random pivot, it avoids the worst-case scenario on sorted data, achieving an expected time complexity of O(n log n) for all inputs.

- [Empirical Analysis](empirical-analysis.md)
This report presents an empirical performance comparison between deterministic and randomized Quicksort. It shows that while both perform similarly on random data, randomized Quicksort significantly outperforms the deterministic version on sorted and reverse-sorted data, confirming the theoretical analysis.

## Sorting with Deterministic Quicksort

To sort a list of numbers using the deterministic quicksort algorithm, run the `deterministic_quick_sort.py` script with the `--elements` argument.

### Example

```bash
python deterministic_quick_sort.py --elements 5 2 8 1 9 4
```

### Sample Output

```
Original array: [5, 2, 8, 1, 9, 4]
Sorted array: [1, 2, 4, 5, 8, 9]
```

## Sorting with Randomized Quicksort

To sort a list of numbers using the randomized quicksort algorithm, run the `randomized_quick_sort.py` script with the `--elements` argument.

### Example

```bash
python randomized_quick_sort.py --elements 5 2 8 1 9 4
```

### Sample Output

```
Original array: [5, 2, 8, 1, 9, 4]
Sorted array: [1, 2, 4, 5, 8, 9]
```

## Emprical Performance Analysis

To run the performance analysis, execute the following command:

```bash
python performance_analysis.py
```

### Sample Output

The script will print a markdown table with the execution times for different input sizes and distributions.

```
| Input Size | Distribution | Algorithm | Execution Time (s) |
|---|---|---|---|
| 10 | random | deterministic | 0.000012 |
| 10 | random | randomized | 0.000015 |
| 10 | sorted | deterministic | 0.000009 |
| 10 | sorted | randomized | 0.000014 |
| 10 | reverse-sorted | deterministic | 0.000009 |
| 10 | reverse-sorted | randomized | 0.000012 |
...
```

