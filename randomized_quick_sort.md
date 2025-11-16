
# Analysis of Randomized Quicksort

Randomized Quicksort is a variation of the Quicksort algorithm that introduces an element of randomness to improve its performance and reliability. 

## The Drawback of Deterministic Quicksort

In a deterministic implementation of the Quicksort algorithm, the pivot selection follows a predefined rule, such as consistently choosing the last element of the array. This deterministic behavior introduces a notable limitation, as predictable pivot selection can lead to suboptimal performance. Specifically, when the input dataset is already sorted or reverse-sorted, the algorithm consistently encounters its worst-case time complexity of O(n²). Consequently, an adversarial entity could exploit this predictability by constructing input sequences designed to intentionally degrade the algorithm’s efficiency.

## How Randomization Works

Randomized Quicksort mitigates the limitations of the deterministic approach by introducing randomness into the pivot selection process, thereby rendering the choice of pivot unpredictable. The central objective is to increase the likelihood of selecting an effective pivot that produces well-balanced partitions on average, regardless of the initial ordering of the input array.

Two primary strategies are used to incorporate randomization:

1.  **Randomly Shuffle the Array:** Prior to sorting, the entire array is randomly permuted. A standard deterministic Quicksort algorithm is then applied to the shuffled data.
2.  **Random Pivot Selection:** At each recursive step, a pivot is randomly selected from the current subarray.

The implementation discussed here adopts the second approach, wherein a random index is chosen, the corresponding element is swapped with the last element, and the standard Lomuto partitioning scheme is subsequently executed.

```python
import random

def randomize_partition(arr, low, high):
    # pick a random pivot and swap with the last element
    pivot_index = random.randint(low, high)
    # Swap the pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # partition the array based on the random pivot and return the partition index
    return partition(arr, low, high)

def quick_sort(arr, low, high):
    if low < high:
        pi = randomize_partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
```

## Performance Implications and Mitigation of the Worst Case

Randomized pivot selection significantly reduces the predictability of the algorithm’s behavior, preventing any specific input configuration from consistently inducing worst-case performance.

- **Expected Time Complexity:** The principal advantage of this approach is that the expected time complexity becomes `O(nlogn)` across all possible input distributions. Importantly, the expectation is taken over the random choices made by the algorithm rather than over the input data itself.

- **Making the Worst-Case Unlikely:** Although the theoretical worst-case complexity of `O(n^2)` remains possible, it occurs only under highly improbable conditions in which the algorithm repeatedly selects the smallest or largest element as the pivot. 

For an array of size `n`, the probability of selecting the worst pivot is `1/n`. Consequently, the probability of making such an unfavorable selection throughout all  `log n` recursive levels is `(1/n)^(log n)`, which rapidly approaches zero as `n` increases.

Because the pivot is chosen randomly, the partition is expected to be reasonably balanced. The algorithm's performance now depends on the random numbers generated during execution, not on the structure of the input data. This makes Randomized Quicksort a more robust and reliable choice in practice compared to its deterministic counterpart.
