# Coding With Kien

def bubble_sort(collection):
    lenght = len(collection)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(lenght - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(lenght - 1 - i):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        # Stop interation if the collection is sorted
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            break
    return collection


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubble_sort(unsorted), sep=" ")
    print(f"Processing time: {time.process_time() - start}")
