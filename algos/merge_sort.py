from random import randint
from sort_test import ARRAY_LENGTH, run_sorting_algorithm


# O(nlog(n))
def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # runs until len(result) == len(left) + len(right)
    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result
# 1 2 4 5 8 10
# 3 6 7 9


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )


if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="merge_sort", array=array)
