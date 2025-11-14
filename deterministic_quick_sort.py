
import argparse

# Function to partition the array on the basis of pivot element
# arr[] --> Array to be partitioned
# low --> Starting index
# high --> Ending index
"""
    This function takes last element as pivot, places the pivot element at its
    correct position in sorted array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right of pivot.
"""
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

# Recursive function to perform quick sort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
def quick_sort(arr, low, high):
    
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deterministic Quicksort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    
    elements = args.elements
    print("Original array:", elements)
    quick_sort(elements, 0, len(elements) - 1)
    print("Sorted array:", elements)