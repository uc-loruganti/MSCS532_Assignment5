
# Analysis of Deterministic Quicksort

Quicksort is a highly efficient, comparison-based, in-place sorting algorithm that adheres to the divide-and-conquer design paradigm. The algorithm operates by selecting a pivot element and partitioning the input array such that all elements smaller than the pivot appear on one side, and all elements larger than the pivot appear on the other.

The implementation analyzed in this study consistently selects the last element of the array as the pivot.

```python
def partition(arr, low, high):
    # Choosing the last element as the pivot
    pivot = arr[high]
    # Index of smaller element
    i = low - 1

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
```

## Time Complexity Analysis

The time complexity of Quicksort depends on the choice of the pivot and the resulting balance of the partitions.

### Worst-Case Time Complexity: O(n^2)

The worst-case scenario arises when the chosen pivot is consistently either the smallest or largest element in the array. For a deterministic implementation that always selects the last element as the pivot, this situation occurs when the input array is already sorted or reverse-sorted.

In this case, the `partition` function divides the array into one sub-array of size `n-1` and another of size `0`.

The recurrence relation for the worst case is:
**T(n) = T(n-1) + O(n)**

- **O(n)**: The `partition` function takes linear time to scan the array of size `n`.
- **T(n-1)**: The recursive call is on a sub-array of size `n-1`.

This recurrence unfolds to:
T(n) = T(n-1) + cn
     = T(n-2) + c(n-1) + cn
     = ...
     = T(1) + c(2 + 3 + ... + n) = n(n-1)/2
     = O(n²)

Hence, the worst-case performance of deterministic Quicksort is comparable to less efficient algorithms such as Insertion Sort or Bubble Sort.

### Best-Case Time Complexity: O(n log n)

The best case occurs when the pivot consistently corresponds to the median element, leading to two evenly divided subarrays. This means the `partition` function splits the array into two equal-sized sub-arrays.

The recurrence relation for the best case is:
**T(n) = 2T(n/2) + O(n)**

- **O(n)**: The `partition` function takes linear time.
- **2T(n/2)**: There are two recursive calls on sub-arrays of size `n/2`.

This is a classic divide-and-conquer recurrence that solves to **O(n log n)**, which can be shown using the Master Theorem. The recursion tree has a depth of `log n`, and at each level, `O(n)` work is done.

### Average-Case Time Complexity: O(n log n)

The average-case analysis considers all possible permutations of the input array. Even if the pivot selection is not perfect, as long as the split is reasonably balanced on average, the complexity remains O(n log n).

For example, if the partition is always split in a 9:1 ratio, the recurrence is:
**T(n) = T(9n/10) + T(n/10) + O(n)**

This recurrence produces a logarithmic recursion depth, yielding an overall time complexity of `O(nlogn)`. It can be mathematically shown that for randomly ordered inputs, the expected runtime achieves this same bound because favorable splits occur frequently enough to dominate the computation cost.

## Space Complexity Analysis

The space complexity is determined by the depth of the recursion stack.

### Worst-Case Space Complexity: O(n)

Similar to the worst-case time complexity, the worst-case space complexity occurs when the array is partitioned into a sub-array of size `n-1` and a sub-array of size `0`. This leads to a recursion depth of `n`.

### Best-Case Space Complexity: O(log n)

The best-case space complexity occurs when the partitions are perfectly balanced, leading to a recursion depth of `log n`.

### Additional Overheads

Quicksort is classified as an in-place sorting algorithm since it performs element swaps within the original array rather than requiring additional auxiliary arrays. The primary overhead arises from recursive function calls, which contribute to stack memory usage. For extremely large input sizes, this recursion depth may lead to stack overflow in the worst case, although such occurrences are uncommon on modern computing systems due to optimized stack management techniques.
