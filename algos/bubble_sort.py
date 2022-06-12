from sort_test import run_sorting_algorithm, ARRAY_LENGTH
from random import randint


# O(n^2)
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        is_sorted = True

        for j in range(n - i - 1):  # -1 to avoid
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False

        if is_sorted:
            break

    return array


if __name__ == '__main__':
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    sorted_array = bubble_sort(array)
    print(array[:20])

    run_sorting_algorithm(algorithm='bubble_sort', array=array)