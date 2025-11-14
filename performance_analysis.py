import timeit
import random
import sys
from deterministic_quick_sort import quick_sort as deterministic_quick_sort
from randomized_quick_sort import quick_sort as randomized_quick_sort

sys.setrecursionlimit(20000)

# Function to generate input data
def generate_input(size, distribution):
    """
    Generates an input array of a given size and distribution.
    """
    if distribution == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverse-sorted":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Invalid distribution type")

# Function to run sorting algorithms and measure execution time
def run_sorting_algorithm(algorithm, data):
    """
    Runs a sorting algorithm on the given data and returns the execution time.
    """
    # Make a copy of the data to avoid sorting the original list
    data_copy = data[:]
    
    # Prepare the sorting function call
    if algorithm == "deterministic":
        sort_func = deterministic_quick_sort
    elif algorithm == "randomized":
        sort_func = randomized_quick_sort
    else:
        raise ValueError("Invalid algorithm type")

    # Time the execution
    start_time = timeit.default_timer()
    sort_func(data_copy, 0, len(data_copy) - 1)
    end_time = timeit.default_timer()
    
    return end_time - start_time

def main():
    """
    Main function to run the performance analysis.
    """
    input_sizes = [10, 50, 100, 200, 500, 1000, 10000]
    distributions = ["random", "sorted", "reverse-sorted"]
    algorithms = ["deterministic", "randomized"]

    print("| Input Size | Distribution | Algorithm | Execution Time (s) |")
    print("|---|---|---|---|")

    for size in input_sizes:
        for dist in distributions:
            for algo in algorithms:
                # Generate the input data
                input_data = generate_input(size, dist)
                
                # Run the sorting algorithm and measure execution time
                execution_time = run_sorting_algorithm(algo, input_data)
                
                # Print the results in a markdown table format
                print(f"| {size} | {dist} | {algo} | {execution_time:.6f} |")

if __name__ == "__main__":
    main()
