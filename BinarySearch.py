import random
import time


# --- Implementation of binary search algorithm
# --- binary search works faster than the native search algorithm

def native_search(l, target):
    # --- Native search in python
    # --- Native search scans  the entire list
    for i in range(len(l)):
        if l[i] == target:
            return i
    return "Number not in list"


def binary_search(l, target, low=None, high=None):
    # --- Binary search uses divide and conquer
    # --- We will leverage the fact that our list is SORTED

    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return "Number not in list"

    # --- Should return 3
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':

    l = [1, 3, 5, 10, 12, 14, 16, 18, 20]
    target = 14  # --- number being searched for
    print("Target number(Native Search) is: ", native_search(l, target))
    print("Target number(Binary Search) is: ", binary_search(l, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    # --- Time it takes to run a binary search for a list
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")

    # --- Time it takes to run a native search for a list
    start = time.time()
    for target in sorted_list:
        native_search(sorted_list, target)
    end = time.time()
    print("Native search time: ", (end - start) / length, "seconds")
