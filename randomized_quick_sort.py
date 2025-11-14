import random
import argparse

# Function to partition the array on the basis of pivot element
def partition(arr, low, high):
    # pivoting the last element as pivot
    pivot = arr[high]
    i = low - 1

    # Traverse through all elements and compare each element with pivot
    for j in range(low, high):
        # If current element is smaller than or equal to pivot, swap it with the element at index i
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot element with the element at index i+1 to place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Return the partition index
    return i + 1

# Randomize partition function
def randomize_partition(arr, low, high):
    # pick a random pivot and swap with the last element
    pivot_index = random.randint(low, high)
    # Swap the pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # partition the array based on the random pivot and return the partition index
    return partition(arr, low, high)


# Recursive function to perform quick sort
# arr[] --> Array to be sorted
# low --> Starting index
# high --> Ending index
def quick_sort(arr, low, high):
    if low < high:
        # partitioning index 
        pi = randomize_partition(arr, low, high)
        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Randomized Quicksort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    
    elements = args.elements
    print("Original array:", elements)
    # Call the randomized quick sort function here
    quick_sort(elements, 0, len(elements) - 1)
    print("Sorted array:", elements)
    